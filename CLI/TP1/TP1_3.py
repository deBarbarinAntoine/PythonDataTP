from TP1 import *


def cli():
    """
    CLI loop for TP1.3 section of Antoine's Python Data TP application.
    
    This function reads data, corrects it, displays the first 5 rows of the corrected data,
    and prompts the user to return to the menu.
    """

    # Read data from a CSV file
    data = read_csv()
    
    # Correct the data using the correct_data function
    corrected_data = correct_data(data)
    
    # Print a header for the corrected data
    print(Style.add('corrected data:', Style.Colors.CYAN, Style.Styles.BOLD))
    
    # Display the first 5 rows of the corrected data
    print(Style.add(str(corrected_data.head()), Style.Colors.BLUE), end='\n\n')
    
    # Prompt the user to return to the menu
    return_menu()
