from TP1 import *


def cli():
	
	corrected_data = correct_data(read_csv())
	
	total_prod_by_type = sum_col_by_colgroup(corrected_data, 'Production_Tonnes', 'Type_Huile')
	print(Style.add(f'The sums of oil production by type are:', Style.Colors.CYAN, Style.Styles.BOLD))
	print(Style.add(str(total_prod_by_type), Style.Colors.BLUE), end = '\n\n')
	
	confirm_continue()
	
	most_productive_year, total_production = col_with_most_col_sum(corrected_data, 'Production_Tonnes', 'Annee')
	print(Style.add(f"The year with the greatest total production is: {most_productive_year}", Style.Colors.CYAN, Style.Styles.BOLD))
	print(Style.add(f"Total production in that year: {total_production}", Style.Colors.CYAN, Style.Styles.BOLD), end = '\n\n')
	
	confirm_continue()
	
	regions_missing_oil = missing_col_values(corrected_data, 'Region', 'Type_Huile')
	print(Style.add(f'The regions with missing produced oil are:', Style.Colors.CYAN, Style.Styles.BOLD))
	for (region, oil) in regions_missing_oil:
		print(Style.add(f'{region}: {oil}', Style.Colors.BLUE))
	print()
	
	return_menu()