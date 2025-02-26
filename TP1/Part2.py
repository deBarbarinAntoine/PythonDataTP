import pandas as pd
from Utils import *

def info(_data: pd.DataFrame) -> tuple:
	print(Style.Colors.BLUE, end = '')
	_data.info()
	print(Style.END, end = '')
	
	return _data.shape

def describe(_data: pd.DataFrame) -> None:
	print(Style.add(str(_data.describe()), Style.Colors.BLUE))