import unittest

from rhs.classes import A, Base
from rhs.utils import print


class TestMethods(unittest.TestCase):
    def test_Base_print(self):
        self.assertEqual(print(Base()), True)
    
    def test_A_print(self):
        self.assertEqual(print(A()), False)


if __name__ == "__main__":
    unittest.main()
