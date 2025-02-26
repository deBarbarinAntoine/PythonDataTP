import pandas as pd


def read_csv() -> pd.DataFrame:
    """
    Reads data from a CSV file named 'production_huile_random.csv'.

    :return: A DataFrame containing the data from the CSV file.
    """
    _data = pd.read_csv('production_huile_random.csv', sep = ',', na_values = '0')
    
    # Uncomment the following line to print the entire DataFrame in blue color
    # print(Style.add(str(_data), Style.Colors.BLUE))
    
    if _data is None:
        exit(1)
        
    return _data


def first_5(_data: pd.DataFrame) -> pd.DataFrame | None:
    """
    Returns the first 5 rows of the given DataFrame.

    :param _data: The input DataFrame.
    :return: A DataFrame containing the first 5 rows of the input DataFrame, or None if the input is None.
    """
    return _data.head()

    