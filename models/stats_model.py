from utils.constants import *
from utils.decorators import validate_integer


class StatsModelClass:
    def __init__(self, captured_numbers):
        self.raw_data = captured_numbers

    @validate_integer
    def less(self, value: int) -> int:
        """
        Get the count of values in a list less than a given value
        :param value: number to compare
        :return: count
        """
        assert value > MIN_VALUE, MIN_VALUE_MESSAGE
        return sum(i < value for i in self.raw_data)

    @validate_integer
    def between(self, left: int, right: int) -> int:
        """
        Get the count of values in a list, given a range of values
        :param left: inferior range
        :param right: superior range
        :return: count
        """
        assert left <= right, INVALID_RANGE_MESSAGE
        return sum(left <= i <= right for i in self.raw_data)

    @validate_integer
    def greater(self, value: int) -> int:
        """
        Get the count of values in a list grater than a given value
        :param value: number to compare
        :return: count
        """
        assert value < MAX_VALUE, MAX_VALUE_MESSAGE
        return sum(i > value for i in self.raw_data)
