from models.stats_model import StatsModelClass
from utils.constants import *
from utils.decorators import validate_integer
from collections import defaultdict


class DataCaptureModelClass:
    def __init__(self) -> None:
        # Defining the dict
        self.__captured_numbers = defaultdict(lambda: 0)

    @validate_integer
    def add(self, value) -> dict:
        """
        Add a new value to the list of values
        :param value: new value to add
        :return: Dict of values
        """
        assert MIN_VALUE <= value <= MAX_VALUE, OUT_RANGE_MESSAGE
        self.__captured_numbers[value] += 1
        return self.__captured_numbers

    def build_stats(self):
        """
        build the stats
        :return:
        """
        count = 0

        # Initialize the indexed dictionaries with all the indexes
        indexed_captured_numbers = defaultdict(
            dict, {k: {LESS_COUNT: 0, GRATER_COUNT: 0} for k in range(MIN_VALUE, MAX_VALUE)}
        )

        for key in indexed_captured_numbers.keys():
            capture_number = self.__captured_numbers.get(key)
            if capture_number:
                indexed_captured_numbers[key] = {GRATER_COUNT: count + 1, LESS_COUNT: count}
                count += capture_number
            else:
                indexed_captured_numbers[key] = {GRATER_COUNT: count, LESS_COUNT: count}
        return StatsModelClass(indexed_captured_numbers, count)

    @property
    def get_values(self):
        return self.__captured_numbers
