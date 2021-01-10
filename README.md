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

## Delivered Files and Directories

The project has the following directory structure:
```
├── data
│   ├── data_description.csv
│   └── raw_data.csv
├── environment.yml
├── notebooks
│   ├── data_exploration.ipynb
│   ├── descriptive_analysis.ipynb
│   └── machine_learning.ipynb
├── output
├── pyproject.toml
├── references
│   └── Second assignment 2020-2021.pdf
├── rendered_notebooks
│   ├── data_exploration.html
│   ├── descriptive_analysis.html
│   └── machine_learning.html
├── setup.py
└── src
    └── ml_colon
        ├── __init__.py
        └── data_preparation.py
```
Here we want to give a brief description of the most relevant files / directories:

The `data` directory is used for storing the input data.

The `environment.yml` contains a list of the needed python packages to run this application. 

The `notebooks` directory contains the main part of the work separated in 3 notebooks:
- `descriptive_analysis.ipynb` where the data is described and univariate analysis is performed
- `data_exploration.ipynb` where the exploratory data analysis is performed
- `machine_learning.ipynb` where the model learning and evaluation is performed

The `rendered_notebooks` directory holds the 3 notebooks but rendered as `.html` files with output.

The `src/ml_colon` directory holds code that is shared between the notebooks. In the `__init__.py` global variables are defined and in the `data_preparation.py` the function to load and clean the data is implemented.

The `output` directory is used to store output of the model training and evaluation process.

The `setup.py` file allows this package to be installed with pip.
