__version__ = '1.0.0'

import string

DEFAULT_ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase


def short(number: int, alphabet: list=DEFAULT_ALPHABET):
    """ Converts an integer to a hexdigest like string -
        except not 16 length but provided alphabet length """
    if not isinstance(number, int):
        raise TypeError('number must be an integer')
    result = ''
    sign = ''
    if number < 0:
        sign = '-'
        number = -number
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        result = alphabet[i] + result
    return result


def expand(string: str, alphabet=DEFAULT_ALPHABET):
    """ Enter hexdigest like string - return integer (base 10) """
    result = 0
    char_list = list(enumerate(string[::-1]))
    for char in char_list:
        result += (alphabet.index(char[1]) * len(alphabet) ** char[0])
    return result
