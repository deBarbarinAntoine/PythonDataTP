import pandas as pd


def sum_col_by_colgroup(_data: pd.DataFrame, col_sum: str, col_group: str):
	return _data.groupby(col_group)[col_sum].sum()

def col_with_most_col_sum(_data: pd.DataFrame, col_sum: str, col_group: str) -> (str, int|float):
	total_col_sum_per_col_group = _data.groupby(col_group)[col_sum].sum()
	
	# Find the col_group with the maximum col_sum
	col_name = total_col_sum_per_col_group.idxmax()
	col_value = total_col_sum_per_col_group.max()
	
	return col_name, col_value

def missing_col_values(_data: pd.DataFrame, col_from: str, col_values: str) -> list:
	# Group by col_from and col_values
	grouped_data = _data.groupby([col_from, col_values]).size().reset_index(name='Count')
	
	# Get all col_from and col_values possible values
	all_from = _data[col_from].unique()
	all_values = _data[col_values].unique()
	
	# Identify missing combinations
	missing_combinations = []
	for val_from in all_from:
		for val_values in all_values:
			if not grouped_data[ (grouped_data[ col_from ] == val_from) & (grouped_data[ col_values ] == val_values) ].empty:
				continue
			missing_combinations.append((val_from, val_values))
	
	return missing_combinations