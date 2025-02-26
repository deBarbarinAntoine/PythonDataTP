import pandas as pd
from Utils import *


def info(_data: pd.DataFrame) -> tuple:
    """
    Prints information about the DataFrame in blue color and returns its shape.

    :param _data: The input DataFrame.
    :return: A tuple containing the number of rows and columns in the DataFrame.
    """
    
    # Set text color to blue
    print(Style.Colors.BLUE, end='')
    
    # Print information about the DataFrame
    _data.info()
    
    # Reset text color
    print(Style.END, end='')
    
    # Return the shape of the DataFrame
    return _data.shape


def describe(_data: pd.DataFrame) -> None:
    """
    Prints a statistical summary of the DataFrame in blue color.

    :param _data: The input DataFrame.
    """
    
    # Print the statistical summary in blue color
    print(Style.add(str(_data.describe()), Style.Colors.BLUE))
