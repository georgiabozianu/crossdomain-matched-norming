Repository Contents: 

This repository contains:
- participant summary data
- trial-level summary statistics
- matched trials
- stimulus information
- this README

All tabular data are provided in Microsoft Excel (.xlsx) or CSV (.csv) format and can be opened using other spreadsheet software (e.g., LibreOffice Calc, VSCode) or statistical software such as R or Python. Scripts can be found at the corresponding GitHub repository: https://github.com/georgiabozianu/crossdomain-matched-norming/tree/main



Participant Information:

Total participants recruited: [152]
Participants included after exclusions: [148]
Mean age: [29]
Age range: [18-40]
Language: [English]
Recruitment method: [Prolific]

Further demographic information is provided in VGTparticipantdata.xlsx.


Semantic Judgement Task (SJT):

Task Description
On each trial, participants were presented with a probe word and asked to select, from three alternatives, the word most closely related in meaning to the probe.

Probe words consisted of nouns and verbs sampled from the English Lexicon Project (Balota et al., 2007). Candidate probe words were selected to span a broad range of psycholinguistic characteristics while approximating the natural distributions observed in English. These characteristics included word frequency, imageability, word length, and syllabic length.

For every probe word, one semantically related target word and two unrelated distractor words were selected and matched on key lexical properties.

Data Files
SJT_stimulus_info_2026.xlsx - contains psycholinguistic information pertaining to each probe word from every trial in the SJT. Variables were obtained from the English Lexicon Project and include lexical characteristics used during stimulus selection.
SJT_subdata.xlsx - contains trial response data (response time, accuracy, response button) from all participants. Sheet 1 = all cleaned data (invalid trials removed); Sheet 2 = all data (invalid trials highlighted).
SJT_trialdata.xlsx - contains trial-level summary statistics aggregated across all participants after exclusion of invalid trials to provide measures such as: mean and SD response time, mean and SD accuracy, Linear Integrated Speed-Accuracy Score (LISAS) and Inverse Efficiency (IE) per trial.


Visuospatial Grid Task (VGT):

Task Description
The Visual Grid Transformation Task (VGT) consists of 1,000 checkerboard-style grid stimuli generated in MATLAB (MathWorks Inc., 2022).

Each trial comprised one probe grid and three comparison grids. Participants were required to identify the comparison grid that matched the probe.

The correct target grid was always visually identical to the probe, although more difficult trials could include spatial transformations. The two distractor grids differed from the probe by the colour of a single grid cell.

Stimuli varied systematically along five perceptual dimensions:

- grid size (3 × 3 or 4 × 4)
- number of colours (2 or 3)
- colour distribution (approximately equal or unequal)
- rotation (0°, 90°, 180°, or 270° clockwise)
- mirror reflection (horizontal or vertical)

These manipulations were designed to produce a wide continuum of visuospatial processing demand while maintaining a consistent trial structure.

Data Files
VGT_participant_data.xlsx - Sheet 1 (Individual Summary): demographic information pertaining to each participant as well as a summary of their performance on the task overall. Sheet 2 (Group Summary): summary statistics of task performance aggregated across the participant sample.
VGT_subdata.xlsx - contains cleaned trial response data (response time, accuracy, response button) from all participants (invalid trials removed) as well as stimulus information regarding the grid properties in each trial.
VGT_trialdata.xlsx -  response data for each grid aggregated across participant group (excluding invalid trials) to provide measures such as: mean and SD response time, mean and SD accuracy per grid (using grid_id as a unique identifier).


Stimulus Filename Conventions
Filenames for VGT stimuli encode the properties of each grid. Probe images have a 6-character code while Target images have 10-character codes (the first 6 characters will be an exact match to the filename of the corresponding probe for that trial). Distractors have a 12-character code (the first 10 characters will be an exact match to the filename of the corresponding target for that trial) and will include unique suffixes(i.e. xxxxxxxxxxD1.png or xxxxxxxxxxD2.png) to denote Distractor 1 (D1) from Distractor 2 (d2) in that trial.

Example probe filename: 'D4C3RU' or D4, C3, RU

A probe filename be broken down into three constituent parts which describe the three principal grid properties. The first letter-digit pair (here 'D4'), denote the grid dimension. D4 means the grid is 4x4 units and D3 means the grid is 3x3. The second letter-digit pair ('C3') denote the number of colours in the grid. C3 means there are 3 colours present (yellow, blue, and white), while C2 would mean that there are 2 colours present (blue and white). The final letter-digit pair ('RU') denote the equality of the ratio of those colours in their distribution across the grid. RU means that there is an unequal ratio of colours in the grid (i.e., one of the colours covers significantly more units of space in the grid than any other). RE would mean that there is a roughly equal spread of the colours present across the grid (e.g., 2 colours may both occupy 8 units within a single 4x4 grid).

Example target filename: 'D4C3RUR0F0' or D4, C3, RU, R0, F0

A target filename can be further broken down to provide an additional two key grid transformations which may impact the difficulty of a given trial. The fourth letter-digit pair in a target filename (here: 'R0') describe whether the target (and both distractors) in this trial have been rotated in space either 90, 180, or 260 degrees clockwise, relative to the probe image. R0 means that no rotation has occurred in this trial, R1 means that a rotation has been applied. The fifth letter-digit pair ('F0') describe whether the target and distractor images in this trial have been 'flipped' (as though mirrored) on either a horizontal or vertical plane, relative to the probe image. F0 means that no flip transformation has occurred, whereas F1 indicates the inverse.


Other Data Files:
matched_trials_data.xlsx - contains the matched items (see 'probe' and 'grid' columns for the unique probe IDs), after cleaning, and summary statistics (response time, accuracy, and standard deviations) for the semantic probe (p), the grid probe (g), and the mean of the semantic and grid probes (m) to depict the quality - or 'closeness' - of the matched pair. 
merged_task_data.csv - contains all cleaned task data from the SJT and VGT merged, including response time and accuracy data for task comparison analyses.

Data Cleaning:
Behavioural datasets are provided in both cleaned and complete forms where applicable.

Cleaned datasets exclude trials classified as invalid according to the pre-processing criteria used in the study.

Invalid trials were defined as: "inattentive or invalid response patterns (e.g., pressing the same button repeatedly or in a systematic sequence)". Trials exhibiting such patterns were excluded prior to analysis.

Examples may include:

- incorrect responses
- anticipatory responses
- omitted responses
- technical errors


Declarations:
Response time is reported in milliseconds (ms).

Accuracy is coded as 0/1, FALSE/TRUE.

Participant IDs and trial identifiers are consistent across datasets wherever applicable (although this was a between-subjects comparison across tasks and so will not correspond from SJT to VGT).

Missing data (e.g. null responses) are represented as blank cells.

Stimulus images are provided as PNG files.

Full methodological details are available in: [manuscript citation available once published after peer-review]
DOI: [""]

If you use these materials in published work, please cite both the accompanying manuscript and the OSF repository.



For questions regarding these materials, please contact:

Name: Ajay Halai
Institution: University of Cambridge, MRC Cognition & Brain Sciences Unit
Email: Ajay.Halai@mrc-cbu.cam.ac.uk

