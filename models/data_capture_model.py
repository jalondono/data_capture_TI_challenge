from models.stats_model import StatsModelClass


class DataCaptureModelClass:
    __captured_numbers = []

    def add(self, value):
        """
        Add a new value to the list of values
        :param value: new value to add
        :return: List of values
        """
        return self.__captured_numbers.append(value)

    def build_stats(self):
        """
        build the stats
        :return:
        """
        return StatsModelClass(self.__captured_numbers)
