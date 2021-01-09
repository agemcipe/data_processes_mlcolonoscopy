# data_processes_mlcolonoscopy


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

## Running MlFlow Dashboard
The model training output from `machine_learning.ipynb` is stored in a local directory `data_processes_mlcolonoscopy/output` by the `mlflow` library. To run the dashboard you can execute 
```
cd output
mlflow ui
```
Make sure you have the right environment enabled.