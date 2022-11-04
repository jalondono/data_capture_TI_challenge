from models.stats_model import StatsModelClass
from utils.constants import *
from utils.decorators import validate_integer


class DataCaptureModelClass:
    def __init__(self) -> None:
        self.__captured_numbers = {}

    @validate_integer
    def add(self, value):
        """
        Add a new value to the list of values
        :param value: new value to add
        :return: List of values
        """
        assert MIN_VALUE <= value <= MAX_VALUE, OUT_RANGE_MESSAGE
        if value not in self.__captured_numbers:
            self.__captured_numbers[value] = 1
        else:
            self.__captured_numbers[value] += 1
        return self.__captured_numbers

    def build_stats(self):
        """
        build the stats
        :return:
        """
        indexed_captured_numbers = {}
        count = 0
        for key in sorted(self.__captured_numbers.keys()):
            indexed_captured_numbers[key] = {
                COUNT: count
            }
            count += self.__captured_numbers[key]
        return StatsModelClass(indexed_captured_numbers, count)

    @property
    def get_values(self):
        return self.__captured_numbers
