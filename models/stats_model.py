from utils.constants import *
from utils.decorators import validate_integer, validate_positive_integer


class StatsModelClass:
    def __init__(self, indexed_captured_numbers, count):
        self.indexed_captured_numbers = indexed_captured_numbers
        self.count = count

    @validate_integer
    @validate_positive_integer
    def less(self, value: int) -> int:
        """
        Get the count of values in a list less than a given value
        :param value: number to compare
        :return: count
        """
        assert value > MIN_VALUE, MIN_VALUE_MESSAGE
        return self.indexed_captured_numbers[value][COUNT]

    @validate_integer
    @validate_positive_integer
    def between(self, left: int, right: int) -> int:
        """
        Get the count of values in a list, given a range of values
        :param left: inferior range
        :param right: superior range
        :return: count
        """
        assert left <= right, INVALID_RANGE_MESSAGE
        return self.indexed_captured_numbers[right][COUNT] - self.indexed_captured_numbers[left][COUNT] + 1

    @validate_integer
    @validate_positive_integer
    def greater(self, value: int) -> int:
        """
        Get the count of values in a list grater than a given value
        :param value: number to compare
        :return: count
        """
        assert value < MAX_VALUE, MAX_VALUE_MESSAGE

        return self.count - self.indexed_captured_numbers[value][COUNT] - 1
