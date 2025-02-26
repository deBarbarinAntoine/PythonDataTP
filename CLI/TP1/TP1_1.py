from TP1 import *


def cli():
    """
    Main CLI loop for TP1.1 section of Antoine's Python Data TP application.
    
    This function retrieves data, displays the first 5 rows, and prompts the user to return to the menu.
    """
    
    # Print a message indicating that data is being retrieved
    print(Style.add('Retrieving data...', Style.Colors.CYAN, Style.Styles.BOLD), end='\n\n')
    
    # Read data from a CSV file
    data = read_csv()
    
    # Print a header for the first 5 rows
    print(Style.add('5 first rows:', Style.Colors.CYAN, Style.Styles.BOLD))
    
    # Display the first 5 rows of the data
    print(Style.add(str(first_5(data)), Style.Colors.BLUE))
    
    # Prompt the user to return to the menu
    return_menu()
