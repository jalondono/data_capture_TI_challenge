import unittest

from utils.constants import *
from utils.decorators import validate_integer


class TestTypeValidation(unittest.TestCase):

    def test_integer_validation(self):
        @validate_integer
        def func(num):
            return num
        self.assertEqual(func(1), 1)

    def test_numeric_string_validation(self):
        @validate_integer
        def func(nun):
            return nun

        with self.assertRaises(Exception) as context:
            func(22, '22')
        self.assertTrue(VALIDATE_INTEGER_MESSAGE in str(context.exception))
