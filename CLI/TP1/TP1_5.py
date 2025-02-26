from TP1 import *


def cli():
    """
    CLI loop for TP1.5 section of Antoine's Python Data TP application.
    
    This function reads data, corrects it, performs various analyses on the corrected data,
    and prompts the user to continue or return to the menu.
    """
    
    # Read data from a CSV file and correct it
    corrected_data = correct_data(read_csv())
    
    # Calculate the total production of oil by type
    total_prod_by_type = sum_col_by_colgroup(corrected_data, 'Production_Tonnes', 'Type_Huile')
    print(Style.add(f'The sums of oil production by type are:', Style.Colors.CYAN, Style.Styles.BOLD))
    print(Style.add(str(total_prod_by_type), Style.Colors.BLUE), end = '\n\n')
    
    # Prompt the user to continue
    confirm_continue()
    
    # Find the year with the greatest total production and its corresponding total production
    most_productive_year, total_production = col_with_most_col_sum(corrected_data, 'Production_Tonnes', 'Annee')
    print(Style.add(f"The year with the greatest total production is: {most_productive_year}", Style.Colors.CYAN, Style.Styles.BOLD))
    print(Style.add(f"Total production in that year: {total_production}", Style.Colors.CYAN, Style.Styles.BOLD), end='\n\n')
    
    # Prompt the user to continue
    confirm_continue()
    
    # Identify regions where a particular type of oil has never been produced
    regions_missing_oil = missing_col_values(corrected_data, 'Region', 'Type_Huile')
    print(Style.add(f'The regions with missing produced oil are:', Style.Colors.CYAN, Style.Styles.BOLD))
    for (region, oil) in regions_missing_oil:
        print(Style.add(f'{region}: {oil}', Style.Colors.BLUE))
    print()
    
    # Prompt the user to return to the menu
    return_menu()
