from TP1 import *


def cli():
	
	data = read_csv()
	
	corrected_data = correct_data(data)
	print(Style.add('corrected data:', Style.Colors.CYAN, Style.Styles.BOLD))
	print(Style.add(str(corrected_data.head()), Style.Colors.BLUE), end = '\n\n')
	
	return_menu()