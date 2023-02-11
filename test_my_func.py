from funcs import my_func
import unittest

class Test_my_funcs(unittest.TestCase):
    def test_my_funcs(self):
        self.assertEqual(my_func(5, 8), 40)
        self.assertIsNone(my_func(5, 0))
        

