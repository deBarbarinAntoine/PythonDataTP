import pandas as pd

def read_csv() -> pd.DataFrame:
	_data = pd.read_csv('production_huile_random.csv', sep=',', na_values='0')
	# print(Style.add(str(_data), Style.Colors.BLUE))
	
	if _data is None:
		exit(1)
		
	return _data

def first_5(_data: pd.DataFrame) -> pd.DataFrame | None:
	return _data.head()
	