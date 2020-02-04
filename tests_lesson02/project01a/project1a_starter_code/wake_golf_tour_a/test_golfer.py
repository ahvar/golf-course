import unittest
from golfer import Golfer

class MyTestCase(unittest.TestCase):
    def test_to_sql_date(self):
        # positive test case
        golfer_id = 1
        golfer_name = 'Arthur Vargas'
        golfer_bday = '04-14-83'
        arthur = Golfer(golfer_id, golfer_name, golfer_bday)
        self.assertEqual(str(arthur), '1,Arthur Vargas,04-14-1983')

        # negative test case: a separator




if __name__ == '__main__':
    unittest.main()
