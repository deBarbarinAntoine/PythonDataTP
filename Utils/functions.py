import os


def take_input(msg = ''):
    """
    Prompts the user for input with an optional message.

    :param msg: Optional string to display as a prompt. Defaults to an empty string.
    :return: The user's input as a string.
    """
    val = input(msg)
    return val


def take_float(msg = ''):
    """
    Prompts the user for input and converts it to a float.

    :param msg: Optional string to display as a prompt. Defaults to an empty string.
    :return: The user's input converted to a float.
    """
    while True:
        val = take_input(msg)
        try:
            return float(val)
        except ValueError:
            continue


def take_int(msg=''):
    """
    Prompts the user for input and converts it to an integer.

    :param msg: Optional string to display as a prompt. Defaults to an empty string.
    :return: The user's input converted to an integer.
    """
    while True:
        val = take_input(msg)
        try:
            return int(val)
        except ValueError:
            continue


def set_precision(val, precision=2):
    """
    Rounds the given value to a specified number of decimal places.

    :param val: The value to round.
    :param precision: The number of decimal places to round to. Defaults to 2.
    :return: The rounded value.
    """
    return round(val, precision)


def return_menu():
    """
    Prompts the user to press [ENTER] to return to the menu.
    """
    print("type [ENTER] to return")
    input()
    return


def confirm_continue():
    """
    Prompts the user to press [ENTER] to continue.
    """
    print("type [ENTER] to continue")
    input()
    return


def clear():
    """
    Clears the console screen.

    This function uses 'cls' for Windows and 'clear' for other operating systems.
    """
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # other OS
    else:
        _ = os.system('clear')
