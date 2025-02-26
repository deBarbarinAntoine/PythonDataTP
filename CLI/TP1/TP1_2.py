from TP1 import *


def cli():
    """
    CLI loop for TP1.2 section of Antoine's Python Data TP application.
    
    This function reads data, displays information about the data, describes the data,
    and prompts the user to continue or return to the menu.
    """
    
    # Read data from a CSV file
    data = read_csv()
    
    # Print a header for data information
    print(Style.add('data info:', Style.Colors.CYAN, Style.Styles.BOLD))
    
    # Get the number of rows and columns in the data
    rows, columns = info(data)
    
    # Prompt the user to continue
    confirm_continue()
    
    # Print a header for describing the data
    print(Style.add('describe data:', Style.Colors.CYAN, Style.Styles.BOLD))
    
    # Describe the data
    describe(data)
    print()
    
    # Prompt the user to continue
    confirm_continue()
    
    # Print the line count and column count of the data
    print(Style.add(f'line count: {rows}', Style.Colors.CYAN, Style.Styles.BOLD))
    print(Style.add(f'column count: {columns}', Style.Colors.CYAN, Style.Styles.BOLD))
    print()
    
    # Prompt the user to return to the menu
    return_menu()
