from TP1 import *


def cli():
    """
    CLI loop for TP1.4 section of Antoine's Python Data TP application.
    
    This function reads data, corrects it, performs various analyses on the corrected data,
    and prompts the user to continue or return to the menu.
    """
    
    # Read data from a CSV file and correct it
    corrected_data = correct_data(read_csv())
    
    # Get the number of unique oil types in the corrected data
    nb_oil_types = nb_col_type(corrected_data, 'Type_Huile')
    print(Style.add(f'nb_oil_types: {nb_oil_types}\n', Style.Colors.CYAN, Style.Styles.BOLD))
    
    # Prompt the user to continue
    confirm_continue()
    
    # Find the region with the most rows in the corrected data
    most_common_region = col_value_with_most_lines(corrected_data, 'Region')
    print(Style.add(f"The region with the most rows is: {most_common_region}\n", Style.Colors.CYAN, Style.Styles.BOLD))
    
    # Prompt the user to continue
    confirm_continue()
    
    # Get the first 10 entries where production tonnage is greater than 500
    greater_500 = rows_greater_than(corrected_data, 'Production_Tonnes', 500)
    print(Style.add(f'The first 10 entries with more than 500T oil production are:', Style.Colors.CYAN, Style.Styles.BOLD))
    print(Style.add(str(greater_500.head(10)), Style.Colors.BLUE), end='\n\n')
    
    # Prompt the user to return to the menu
    return_menu()
