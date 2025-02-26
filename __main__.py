from CLI import *


if __name__ == '__main__':
    """
    Entry point of the application.
    
    This block checks if the script is being run as the main program (not imported as a module).
    If it is, it calls the `cli` method from the `CLI.main_menu` object to start the CLI loop.
    Finally, it exits the program with a status code of 0.
    """
    
    # Call the CLI loop
    CLI.main_menu.cli()
    
    # Exit the program with a status code of 0
    exit(0)
