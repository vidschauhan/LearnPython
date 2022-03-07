# Created by vidit.singh at 07-03-2022
import unittest
import Assignment


class MyTestCase(unittest.TestCase):

    def test_square_it(self):
        n1 = 5
        num = Assignment.square_it()
        p1 = n1**2
        self.assertEqual(num, p1)  # add assertion here


if __name__ == '__main__':
    unittest.main()

