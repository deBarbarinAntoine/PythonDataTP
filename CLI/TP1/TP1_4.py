from TP1 import *


def cli():
	
	corrected_data = correct_data(read_csv())
	
	nb_oil_types = nb_col_type(corrected_data, 'Type_Huile')
	print(Style.add(f'nb_oil_types: {nb_oil_types}\n', Style.Colors.CYAN, Style.Styles.BOLD))
	
	confirm_continue()
	
	most_common_region = col_value_with_most_lines(corrected_data, 'Region')
	print(Style.add(f"The region with the most rows is: {most_common_region}\n", Style.Colors.CYAN, Style.Styles.BOLD))
	
	confirm_continue()
	
	greater_500 = rows_greater_than(corrected_data, 'Production_Tonnes', 500)
	print(Style.add(f'The first 10 entries with more than 500T oil production are:', Style.Colors.CYAN, Style.Styles.BOLD))
	print(Style.add(str(greater_500.head(10)), Style.Colors.BLUE), end = '\n\n')
	
	return_menu()