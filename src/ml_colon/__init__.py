import pathlib

# Define some global variables to be available on import


# The path of the directory in which this file is stored
HERE = pathlib.Path(__file__)

# The path of the directory in which the data (csv files) are stored
DATA_DIR = data_dir = HERE.parents[2] / "data"

# The name of the file that contains the raw data set
RAW_CSV_FILENAME = "raw_data.csv"

# The filepath of the raw data set
RAW_CSV_PATH = DATA_DIR / RAW_CSV_FILENAME

# The path of the directory in which the outputs of model trainings are stored
OUTPUT_DIR = HERE.parents[2] / "output"

# The columns that are expected in the raw data set
CSV_HEADER = [
    "quality",
    "bits",
    "intra_parts",
    "skip_parts",
    "inter_16x16_parts",
    "inter_4x4_parts",
    "inter_other_parts",
    "non_zero_pixels",
    "frame_width",
    "frame_height",
    "movement_level",
    "mean",
    "sub_mean_1",
    "sub_mean_2",
    "sub_mean_3",
    "sub_mean_4",
    "var_sub_blocks",
    "sobel_h",
    "sobel_v",
    "variance",
    "block_movement_h",
    "block_movement_v",
    "var_movement_h",
    "var_movement_v",
    "cost_1",
    "cost_2",
    "relevant",
]


# The target variable in the data set
TARGET_VARIABLE = "relevant"

assert TARGET_VARIABLE in CSV_HEADER

# SEED used for random state throughout the application
SEED = 12345

# Score Metrics implemented for sklearn classifiers
SCORE_METRICS = [
    "accuracy",
    "balanced_accuracy",
    "top_k_accuracy",
    "average_precision",
    "neg_brier_score",
    "f1",
    "f1_micro",
    "f1_macro",
    "f1_weighted",
    "f1_samples",
    "neg_log_loss",
    "precision",
    "recall",
    "jaccard",
    "roc_auc",
    "roc_auc_ovr",
    "roc_auc_ovo",
    "roc_auc_ovr_weighted",
    "roc_auc_ovo_weighted",
]
