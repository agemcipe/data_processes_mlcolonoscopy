# data_processes_mlcolonoscopy
The final version of the code is in the branch "release"

## Setup

### Optional (but recommended)
Create a conda environment to run this project in isolation.
```[bash]
cd data_processes_mlcolonoscopy/
conda env create -f environment.yml
conda activate ml_colon
```

### Installation
```[bash]
cd data_processes_mlcolonoscopy/
pre-commit install
pip install --editable .
```

## Input Data
The application expects the input data set under  `data/raw_dat.csv`. The input data set is part of the git repository.

## Running MlFlow Dashboard
The model training output from `machine_learning.ipynb` is stored in a local directory `data_processes_mlcolonoscopy/output` by the `mlflow` library. To run the dashboard you can execute 
```
cd output
mlflow ui
```
Make sure you have the right environment enabled.

## Files
The "data" folder contains the data needed to run the code. 
The folder "notebooks" contains three notebooks:
- descriptive_analysis where the data is described and univariate analysis is performed
- data_exploration where the exploratory data analysis is performed
- machine_learning where the model learning and evaluation is performed

The folder "rendered notebooks" contain the above notebooks in html format. 
The "src" folder contains code used for loading and cleaning the data. 
All the files in the main folder are used for setting up the project environment.
