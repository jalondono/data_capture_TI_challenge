
class StatsModelClass:
    def __init__(self, captured_numbers):
        self.raw_data = captured_numbers

    def less(self, value: int) -> int:
        """
        Get the count of values in a list less than a given value
        :param value: number to compare
        :return: count
        """
        return sum(i < value for i in self.raw_data)

    def between(self, left: int, right: int) -> int:
        """
        Get the count of values in a list, given a range of values
        :param left: inferior range
        :param right: superior range
        :return: count
        """
        return sum(left <= i <= right for i in self.raw_data)

    def greater(self, value: int) -> int:
        """
        Get the count of values in a list grater than a given value
        :param value: number to compare
        :return: count
        """
        return sum(i > value for i in self.raw_data)
