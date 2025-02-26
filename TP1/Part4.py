import pandas as pd


def nb_col_type(_data: pd.DataFrame, col: str) -> int:
    """
    Returns the number of unique values in a specified column of the DataFrame.

    :param _data: The input DataFrame.
    :param col: The name of the column to check for unique values.
    :return: The number of unique values in the specified column.
    """
    return _data[ col ].nunique()


def col_value_with_most_lines(_data: pd.DataFrame, col: str) -> str:
    """
    Returns the value that appears most frequently in a specified column of the DataFrame.

    :param _data: The input DataFrame.
    :param col: The name of the column to check for the most frequent value.
    :return: The value that appears most frequently in the specified column.
    """
    region_counts = _data[col].value_counts()
    
    # Return the region with the most rows
    return region_counts.idxmax()


def rows_greater_than(_data: pd.DataFrame, col: str, val) -> pd.DataFrame:
    """
    Returns rows where the values in a specified column are greater than a given threshold.

    :param _data: The input DataFrame.
    :param col: The name of the column to check for values greater than the threshold.
    :param val: The threshold value.
    :return: A DataFrame containing rows where the specified column's values are greater than the threshold.
    """
    return _data[_data[col] > val]
