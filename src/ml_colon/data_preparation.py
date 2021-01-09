# type: ignore

import pathlib

import pandas as pd

import ml_colon

THRESHOLD = 0.01


def get_df_from_csv(filepath: pathlib.Path = ml_colon.RAW_CSV_PATH) -> pd.DataFrame:
    """Read csv file into DataFrame.

    Parameters
    ----------
    filepath : pathlib.Path, optional
        [description], by default ml_colon.RAW_CSV_PATH

    Returns
    -------
    pd.DataFrame
        the raw data in a DataFrame
    """
    return pd.read_csv(filepath, header=0, names=ml_colon.CSV_HEADER)


def remove_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """Remove the rows with null values when they are less than the threshold.

    Parameters
    ----------
    df : pd.DataFrame
        [description]

    Returns
    -------
    pd.DataFrame
        the cleaned DataFrame
    """
    # remove rows with null values making up less than 1% of the total rows
    cols_to_dropna = []
    has_nulls = df.columns[df.isnull().any()]

    for each in has_nulls:
        if df[each].isnull().sum() < df[each].count() * THRESHOLD:
            cols_to_dropna.append(each)
    return df.dropna(subset=cols_to_dropna)


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """Clean DataFrame from unreasonable obversations.

    Parameters
    ----------
    df : pd.DataFrame
        [description]

    Returns
    -------
    pd.DataFrame
        the cleaned DataFrame
    """
    # remove rows with null values in target variable
    df = df[~df[ml_colon.TARGET_VARIABLE].isnull()]

    return df


def get_clean_df_from_csv(
    filepath: pathlib.Path = ml_colon.RAW_CSV_PATH,
) -> pd.DataFrame:
    """Get DataFrame from csv and clean it.

    Parameters
    ----------
    filepath : pathlib.Path, optional
        [description], by default ml_colon.RAW_CSV_PATH

    Returns
    -------
    pd.DataFrame
        the cleaned DataFrame
    """
    no_nulls_in_target = clean_df(get_df_from_csv(filepath))
    nulls_removed = remove_nulls(no_nulls_in_target)
    return nulls_removed
