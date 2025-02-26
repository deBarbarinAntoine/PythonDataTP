import pandas as pd


def nb_col_type(_data: pd.DataFrame, col: str) -> int:
	return _data[col].nunique()

def col_value_with_most_lines(_data: pd.DataFrame, col: str) -> str:
	region_counts = _data[col].value_counts()
	
	# Return the region with the most rows
	return region_counts.idxmax()

def rows_greater_than(_data: pd.DataFrame, col: str, val) -> pd.DataFrame:
	return _data[_data[col] > val]