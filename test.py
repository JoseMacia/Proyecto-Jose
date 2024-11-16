import unittest

class TestSum(unittest.TestCase):
def test_sum(self):
self.assertEqual(sum(1,2), 3)

if__name__=='__main__':
unittest.main()
