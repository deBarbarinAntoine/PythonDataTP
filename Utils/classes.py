from Utils.functions import *


class Style:
    """
    The class Style provides a way of defining a color or style in the terminal.
    """
    # Nested class for different colors available in the terminal
    class Colors:
        BLUE = '\033[94m'  # Blue color code
        CYAN = '\033[38;2;0;255;255m'  # Cyan color code
        GREEN = '\033[92m'  # Green color code
        YELLOW = '\033[93m'  # Yellow color code
        RED = '\033[91m'  # Red color code
    
    # Nested class for different styles available in the terminal
    class Styles:
        BOLD = '\033[1m'  # Bold style code
        UNDERLINE = '\033[4m'  # Underline style code
    
    END = '\033[0m'  # Reset all attributes to their defaults

    @staticmethod
    def add(string: str, color: Colors = None, *styles: Styles | None) -> str:
        """
        Adds a color or styles to the given string.

        :param string: The input string to which colors/styles will be added.
        :param color: Optional color from the Colors class. Defaults to None.
        :param styles: Optional styles from the Styles class. Can be multiple, defaults to None.
        :return: The modified string with applied colors and styles.
        """
        if color is None and not styles:
            return string  # Return original string if no color or style is provided

        if color:
            string = f'{color}{string}'  # Add the specified color to the string

        if styles:
            for style in styles:
                if style:
                    string = f'{style}{string}'  # Add each specified style to the string

        return f'{string}{Style.END}'  # Reset all attributes after adding colors and styles
    

class MenuCLI:
    """
    The Menu class provides a way of handling a simple menu in CLI.
    """
    def __init__(self):
        self._title = ''
        self._options = []
        self._exit_option = None
        self._width_max = 0
    
    @staticmethod
    def new(*options, title = 'Menu', exit_option = None):
        """
        The new method creates a new menu object.
        :param options: the list of options available in the menu.
        :param title: the title of the menu.
        :param exit_option: the label of the exit option.
        :return: the new menu object.
        """
        menu = MenuCLI()
        menu._options = options
        menu._title = title
        menu._width_max = len(title)
        i: int = 0
        for option in options:
            i += 1
            if len(f'{i}/ {option}') > menu._width_max:
                menu._width_max = len(f'{i}/ {option}')
        if exit_option is not None:
            menu._exit_option = exit_option
        return menu
    
    def run(self) -> int:
        """
        The run method starts the menu.
        :return: the integer associated with the option chosen by the user.
        """
        clear()
        print(Style.add(f'{self._title:^{self._width_max}}', Style.Colors.CYAN, Style.Styles.BOLD))
        print('▔' * self._width_max)
        i: int = 0
        for option in self._options:
            i += 1
            print(f'{i}/ {option}')
        exit_label = 'Exit'
        if self._exit_option is not None:
            exit_label = self._exit_option
        print(Style.add(f'0/ {exit_label}', Style.Colors.RED))
        while True:
            res = take_int('> ')
            if 0 <= res <= len(self._options):
                return res