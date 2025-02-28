from CLI import *
from Utils import *


def cli():
    """
    Main CLI loop for Antoine's Python Data TP application.
    
    This function displays a main menu and handles user input using a match-case statement.
    It provides options to load and explore data, understand data structure, identify and handle missing data,
    perform rapid exploration, and access advanced topics.
    """
    
    while True:
        print('-' * 31)
        # Display welcome message with style
        print(Style.add(f"Welcome to Antoine's Python Data TP!"), Style.Colors.CYAN, Style.Styles.BOLD)
        print('-' * 31)
        
        # Create a new menu with options and title
        menu = MenuCLI.new(
            'TP1.1 Load and explore the data',
            'TP1.2 Understand the data structure',
            'TP1.3 Identify and handle missing data',
            'TP1.4 Rapid exploration',
            'TP1.5 Advanced topics',
            'TP2.1 Probabilities and statistics',
            title='Main Menu'
        )

        # Run the menu and handle user input
        match menu.run():
            case 0:
                print("Bye!")
                exit(0)  # Exit the application if user selects option 0 (Exit)
            case 1:
                TP1_1.cli()  # Call CLI for TP1.1
            case 2:
                TP1_2.cli()  # Call CLI for TP1.2
            case 3:
                TP1_3.cli()  # Call CLI for TP1.3
            case 4:
                TP1_4.cli()  # Call CLI for TP1.4
            case 5:
                TP1_5.cli()  # Call CLI for TP1.5
            case 6:
                TP2_1.cli()  # Call CLI for TP2.1
