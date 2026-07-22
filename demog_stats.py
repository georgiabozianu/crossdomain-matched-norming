import pandas as pd
import numpy as np
from scipy.special import gammaln
import pingouin as pg
import os

# File names
print("Loading data for demographic statistics")
workdir = ""            #set your working directory here with access to the SJT and VGT subject data files
file_sj = os.path.join(workdir, "SJT/derivatives/results/SJT_subdata.xlsx")
file_vg = os.path.join(workdir, "VGT/derivatives/results/VGT_subdata.xlsx")

# Check required columns
required_cols = ["subject_ID", "age", "sex"]

def load_and_clean(file):
    df = pd.read_excel(file)

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"{file} is missing column: {col}")

    # Group by subject_ID
    df_grouped = df.groupby("subject_ID")[["age", "sex"]].first().reset_index()

    return df_grouped

# Load data
sj = load_and_clean(file_sj)
vg = load_and_clean(file_vg)

# ---------- AGE (Bayesian independent t-test) ----------
age_sj = sj["age"].dropna()
age_vg = vg["age"].dropna()

print("SJ Age: mean =", age_sj.mean(), ", SD =", age_sj.std())
print("VG Age: mean =", age_vg.mean(), ", SD =", age_vg.std())

age_test = pg.ttest(age_sj, age_vg, paired=False)
age_test_row = age_test.iloc[0]

def interpret_bayes_factor(bf10):
    if pd.isna(bf10):
        return "Bayes factor unavailable"
    if bf10 < 1 / 3:
        return "evidence for the null"
    if bf10 < 1:
        return "anecdotal evidence for the null"
    if bf10 < 3:
        return "anecdotal evidence for the alternative"
    if bf10 < 10:
        return "moderate evidence for the alternative"
    return "strong evidence for the alternative"

print("\nBayesian t-test (Age):")
print("t =", age_test_row["T"])
print("p =", age_test_row["p-val"])
print("BF10 =", age_test_row["BF10"])
print("Cohen's d =", age_test_row["cohen-d"])


# ---------- SEX (Bayesian contingency table) ----------
# Combine groups with label
sj["group"] = "SJ"
vg["group"] = "VG"

combined = pd.concat([sj, vg])

# Drop missing
combined = combined.dropna(subset=["sex"])

# Contingency table
contingency = pd.crosstab(combined["group"], combined["sex"])

print("\nContingency Table (Sex):")
print(contingency)

# Bayesian contingency-table comparison: saturated vs independence model
def bayes_factor_contingency(table, alpha=0.5):
    table = np.asarray(table, dtype=float)
    if table.ndim != 2:
        raise ValueError("Contingency table must be two-dimensional")

    row_sums = table.sum(axis=1)
    col_sums = table.sum(axis=0)
    total = table.sum()

    def log_dirichlet_multinomial(counts, prior):
        counts = np.asarray(counts, dtype=float)
        prior = np.asarray(prior, dtype=float)
        return (
            gammaln(prior.sum())
            - gammaln(total + prior.sum())
            + np.sum(gammaln(counts + prior) - gammaln(prior))
        )

    saturated_prior = np.full(table.size, alpha)
    row_prior = np.full(table.shape[0], alpha)
    col_prior = np.full(table.shape[1], alpha)

    log_m_sat = log_dirichlet_multinomial(table.ravel(), saturated_prior)
    log_m_ind = log_dirichlet_multinomial(row_sums, row_prior) + log_dirichlet_multinomial(col_sums, col_prior)

    return np.exp(log_m_sat - log_m_ind)


sex_bf10 = bayes_factor_contingency(contingency.to_numpy(), alpha=0.5)

# Print Results
print("\nBayesian contingency-table test (Sex):")
print("BF10 =", sex_bf10)
print("Evidence =", interpret_bayes_factor(sex_bf10))
print("SJT Mean Age =", age_sj.mean())
print("VGT Mean Age =", age_vg.mean())

    