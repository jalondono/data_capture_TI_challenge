import unittest

from utils.constants import *
from models.data_capture_model import DataCaptureModelClass


class StatsModelTests(unittest.TestCase):

    def setUp(self) -> DataCaptureModelClass:
        self.data_capture = DataCaptureModelClass()
        self.data_capture.add(3)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(6)
        self.data_capture.add(9)
        return self.data_capture

    def test_less(self):
        stats = self.data_capture.build_stats()
        less = stats.less(4)
        self.assertEqual(less, 2)

    def test_less_negative(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(Exception) as context:
            less = stats.less(-4)
        self.assertTrue(MIN_VALUE_MESSAGE in str(context.exception))

    def test_less_invalid_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(Exception) as context:
            less = stats.less('x')
        self.assertTrue(VALIDATE_INTEGER_MESSAGE in str(context.exception))

    def test_greater(self):
        stats = self.data_capture.build_stats()
        greater = stats.greater(4)
        self.assertEqual(greater, 2)

    def test_greater_negative(self):
        stats = self.data_capture.build_stats()
        greater = stats.greater(-4)
        self.assertEqual(greater, len(self.data_capture.get_values))

    def test_greater_invalid_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(Exception) as context:
            greater = stats.greater('x')
        self.assertTrue(VALIDATE_INTEGER_MESSAGE in str(context.exception))

    def test_between(self):
        stats = self.data_capture.build_stats()
        between = stats.between(3, 6)
        self.assertEqual(between, 4)

    def test_between_negative_range(self):
        stats = self.data_capture.build_stats()
        between = stats.between(-6, 4)
        self.assertEqual(between, 3)

    def test_between_inverse_range(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(Exception) as context:
            between = stats.between(6, 3)
        self.assertTrue(INVALID_RANGE_MESSAGE in str(context.exception))

    def test_between_invalid_value(self):
        stats = self.data_capture.build_stats()
        with self.assertRaises(Exception) as context:
            between = stats.between('x', 1)
        self.assertTrue(VALIDATE_INTEGER_MESSAGE in str(context.exception))
