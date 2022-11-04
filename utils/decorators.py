from utils.constants import *


def validate_integer(func):
    """
    Decorator function to validate the passed arguments are integers
    :param func: function to wrap
    :return: Wrapped function
    """
    def wrapper(*args):
        numbers_list = args[1:]
        if not all(isinstance(number, int) for number in numbers_list):
            raise ValueError(
                VALIDATE_INTEGER_MESSAGE
            )
        return func(*args)
    return wrapper


def validate_positive_integer(func):
    """
    Decorator function to validate the passed arguments positive integers
    :param func: function to wrap
    :return: Wrapped function
    """
    def wrapper(*args):
        numbers_list = args[1:]
        if not all(number >= 0 for number in numbers_list):
            raise ValueError(
                NEGATIVE_RANGE_MESSAGE
            )
        return func(*args)
    return wrapper
