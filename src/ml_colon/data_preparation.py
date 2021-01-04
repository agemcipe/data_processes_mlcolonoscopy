import pathlib

import pandas as pd

import ml_colon


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
    return clean_df(get_df_from_csv(filepath))
