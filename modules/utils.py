import time
import random

import termcolor


ALPHABET = "abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ\
0123456789\
?,;. :/!*$^=+~#\"'([-|`_\\@)]{}"


class CharNotSupportedError(Exception):
    pass



def cool_print(text : str, wait_time : float = 0.01, color : str = "white", charset : str = ALPHABET, no_errors : bool = False) -> None :
    """Another print function but it looks cool

    Args:
        word (str): the word you want to cool print
        wait_time (float): the time you want to wait between each char guess (NOT BETWEEN EACH CHAR PRINT, IT'S RANDOM)
        color (str): the color in which you want to print your cool text, see termcolor availible colors
        charset (str): the chars that actually can be printed
        no_errors (bool): if set to 'True', will not show error and add not supported char to 'charset'

    Raises:
        CharNotExistingError: if the word contains one or more letter that are not present in 'ALPHABET' constant
    """

    for char in text:
        if char == '\n':
            continue

        if not char in charset:
            if no_errors:
                charset += char
            else:
                raise CharNotSupportedError(f"one of the char you put in parameter 'word' ('{char}') is not supported, but you can set the 'charset' parameter to include the chars not included by default")


    to_print = ""
    random_choosed = ''

    for line in text.split('\n'):
        for char in line:
            while not random_choosed == char:
                random_choosed = random.choice(charset)

                colored_text = termcolor.colored(f"{to_print}{random_choosed}\r", color)
                print(colored_text, end='')

                time.sleep(wait_time)

            to_print += random_choosed

        to_print = ""
        print()

    colored_text = termcolor.colored(to_print, color)
    print(colored_text)

