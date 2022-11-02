from models.stats_model import StatsModelClass
from utils.constants import *
from utils.decorators import validate_integer


class DataCaptureModelClass:
    def __init__(self) -> None:
        self.__captured_numbers = []

    @validate_integer
    def add(self, value):
        """
        Add a new value to the list of values
        :param value: new value to add
        :return: List of values
        """
        assert MIN_VALUE <= value <= MAX_VALUE, OUT_RANGE_MESSAGE
        return self.__captured_numbers.append(value)

    def build_stats(self):
        """
        build the stats
        :return:
        """
        return StatsModelClass(self.__captured_numbers)

    @property
    def get_values(self):
        return self.__captured_numbers
