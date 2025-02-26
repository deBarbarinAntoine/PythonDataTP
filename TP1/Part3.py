import pandas as pd


def correct_data(_data: pd.DataFrame) -> pd.DataFrame:
    """
    Corrects the data by filling NaN values in 'Production_Tonnes' with 0 and
    replacing NaN values in 'Prix_Moyen_Tonne' with the mean price for each type of oil.

    :param _data: The input DataFrame containing production data.
    :return: A corrected DataFrame with filled NaN values.
    """
    
    # Fill NaN values in 'Production_Tonnes' with 0
    _data[ 'Production_Tonnes' ] = _data['Production_Tonnes'].fillna(0)
    
    # Calculate the mean of 'Prix_Moyen_Tonne' grouped by 'Type_Huile'
    mean_prices = _data.groupby('Type_Huile')['Prix_Moyen_Tonne'].transform('mean')
    
    # Fill NaN values in 'Prix_Moyen_Tonne' with the calculated mean
    _data['Prix_Moyen_Tonne'] = _data['Prix_Moyen_Tonne'].fillna(mean_prices)
    
    return _data
