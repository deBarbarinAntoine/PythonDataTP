import pandas as pd


def sum_col_by_colgroup(_data: pd.DataFrame, col_sum: str, col_group: str) -> pd.Series:
    """
    Sums the values of one column grouped by another column.

    :param _data: The input DataFrame.
    :param col_sum: The name of the column to sum.
    :param col_group: The name of the column to group by.
    :return: A Series with the sums, indexed by the grouping column.
    """
    return _data.groupby(col_group)[ col_sum ].sum()


def col_with_most_col_sum(_data: pd.DataFrame, col_sum: str, col_group: str) -> (str, int | float):
    """
    Finds the group with the maximum sum in a specified column.

    :param _data: The input DataFrame.
    :param col_sum: The name of the column to sum.
    :param col_group: The name of the column to group by.
    :return: A tuple containing the group name and its sum.
    """
    total_col_sum_per_col_group = _data.groupby(col_group)[ col_sum ].sum()
    
    # Find the col_group with the maximum col_sum
    col_name = total_col_sum_per_col_group.idxmax()
    col_value = total_col_sum_per_col_group.max()
    
    return col_name, col_value


def missing_col_values(_data: pd.DataFrame, col_from: str, col_values: str) -> list:
    """
    Identifies missing combinations of values in two columns.

    :param _data: The input DataFrame.
    :param col_from: The name of the first column to check for missing combinations.
    :param col_values: The name of the second column to check for missing combinations.
    :return: A list of tuples representing the missing combinations.
    """
    # Group by col_from and col_values
    grouped_data = _data.groupby([col_from, col_values]).size().reset_index(name='Count')
    
    # Get all col_from and col_values possible values
    all_from = _data[col_from].unique()
    all_values = _data[col_values].unique()
    
    # Identify missing combinations
    missing_combinations = []
    for val_from in all_from:
        for val_values in all_values:
            if not grouped_data[(grouped_data[col_from] == val_from) & (grouped_data[col_values] == val_values)].empty:
                continue
            missing_combinations.append((val_from, val_values))
    
    return missing_combinations
