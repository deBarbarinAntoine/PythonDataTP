import numpy as np
import pandas as pd

def readCSV() -> pd.DataFrame|None:
    _data = pd.read_csv('production_huile_random.csv', sep=',', na_values='0')
    # print(_data)
    return _data

def print5(_data: pd.DataFrame) -> None:
    five = _data.head()
    print(five)

def info(_data: pd.DataFrame) -> None:
    print(_data.info())
    rows, columns = _data.shape
    print(f'line count: {rows}\n')
    print(f'column count: {columns}\n')

def describe(_data: pd.DataFrame) -> None:
    print(_data.describe())

def correct_data(_data: pd.DataFrame) -> pd.DataFrame:
    # Fill NaN values in 'Production_Tonnes' with 0
    _data['Production_Tonnes'].fillna(0, inplace=True)

    # Calculate the mean of 'Prix_Moyen_Tonne' grouped by 'Type_Huile'
    mean_prices = _data.groupby('Type_Huile')['Prix_Moyen_Tonne'].transform('mean')

    # Fill NaN values in 'Prix_Moyen_Tonne' with the calculated mean
    _data['Prix_Moyen_Tonne'].fillna(mean_prices, inplace=True)

    return _data

def nb_col_type(_data: pd.DataFrame, col: str) -> int:
    return _data[col].nunique()

def col_value_with_most_lines(_data: pd.DataFrame, col: str) -> str:
    region_counts = _data[col].value_counts()

    # Return the region with the most rows
    return region_counts.idxmax()

def rows_greater_than(_data: pd.DataFrame, col: str, val) -> pd.DataFrame:
    return _data[_data[col] > val]

def sum_col_by_colgroup(_data: pd.DataFrame, col_sum: str, col_group: str):
    return _data.groupby(col_group)[col_sum].sum()

def col_with_most_col_sum(_data: pd.DataFrame, col_sum: str, col_group: str) -> (str, int|float):
    total_col_sum_per_col_group = _data.groupby(col_group)[col_sum].sum()

    # Find the col_group with the maximum col_sum
    col_name = total_col_sum_per_col_group.idxmax()
    col_value = total_col_sum_per_col_group.max()

    return col_name, col_value

if __name__ == '__main__':
    data = readCSV()
    if data is not None:
        print('5 first rows:\n')
        print5(data)

        print('data info:\n')
        info(data)

        print('describe data:\n')
        describe(data)

        corrected_data = correct_data(data)
        print('corrected data:\n')
        print(corrected_data.head())

        nb_oil_types = nb_col_type(corrected_data, 'Type_Huile')
        print(f'nb_oil_types: {nb_oil_types}\n')

        most_common_region = col_value_with_most_lines(corrected_data, 'Region')
        print(f"The region with the most rows is: {most_common_region}\n")

        greater_500 = rows_greater_than(corrected_data, 'Production_Tonnes', 500)
        print(greater_500.head(10))

        total_prod_by_type = sum_col_by_colgroup(corrected_data, 'Production_Tonnes', 'Type_Huile')
        print(total_prod_by_type)

        most_productive_year, total_production = col_with_most_col_sum(corrected_data, 'Production_Tonnes', 'Annee')
        print(f"The year with the greatest total production is: {most_productive_year}")
        print(f"Total production in that year: {total_production}")

    exit(0)