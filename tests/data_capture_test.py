import unittest

from models.data_capture_model import DataCaptureModelClass
from utils.constants import *


class DataCaptureTests(unittest.TestCase):

    def test_add_a_number_correctly(self):
        """
        Test tha can be added a number using the add method from DataCaptureModelClass correctly
        """
        values_to_add = [0, 1, 2, 3, 999]
        expected_value = {0: 1, 1: 1, 2: 1, 3: 1, 999: 1}

        added_values = []
        instance = DataCaptureModelClass()
        for value in values_to_add:
            instance.add(value)

        self.assertDictEqual(instance.get_values, expected_value)

    def test_add_invalid_value_fail(self):
        """
        Test that can't be added an invalid value and an error is raised
        """
        values_to_add = ['0', -11, 1111]
        expected_messages = [VALIDATE_INTEGER_MESSAGE, OUT_RANGE_MESSAGE, OUT_RANGE_MESSAGE]
        instance = DataCaptureModelClass()
        for idx, value in enumerate(values_to_add):
            with self.assertRaises(Exception) as context:
                instance.add(value)
            self.assertTrue(expected_messages[idx] in str(context.exception))
