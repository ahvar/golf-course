import unittest
import os
import time
from golfer import Golfer


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        This method can be used to define fields which will be used throughout the test class. This method runs once.
        :return:
        """
        # Save the current directory so we know the path to the source. This is used for running the program through
        # the command line. It's also used to reset the current working directory after a test completes.
        cls._current_directory = os.getcwd()
        # probably don't need this since golfer is not run from the command line
        cls._golfer_abs_path = os.path.join(cls._current_directory, "golfer.py")

        timestamp = time.strftime("%Y%m%d%H%M%S")
        classname = cls.__name__
        results_dir = "output-{}-{}".format(classname, timestamp)
        cls._output_dir = results_dir
        if not os.path.exists(cls._output_dir):
            os.makedirs(cls._output_dir)

        cls._output_path = os.path.join(cls._current_directory, cls._output_dir)
        os.chdir(cls._output_path)

    def setUp(self):
        """
        Setup for test case. This repeated for each test case.
        :return:
        """
        os.chdir(self._output_path)
        self.golfer_id = 1
        self.golfer_name = 'Arthur Vargas'
        self.golfer_bday = '04-14-83'
        self.arthur = Golfer(self.golfer_id, self.golfer_name, self.golfer_bday)
        # the birthday format is not valid
        # arthur_invalid_bday = Golfer(golfer_id, golfer_name, "04 14 83")
        # the name is invalid
        # arthur_invalid_name = Golfer(golfer_id, "Ar$thur Vargas", "04-14-83")

    @classmethod
    def tearDownClass(cls):
        os.chdir(cls._current_directory)


    def test_to_sql_date(self):
        # positive test case
        try:
            self.assertEqual(str(self.arthur), '1,Arthur Vargas,04-14-1983')
        except Exception as ex:
            self.fail(f'An {ex} was thrown when it should not have been')

        # negative test case: whitespace is an invalid separator
        invalid_bday = '04 14 83'
        try:
            arthur_invalid_bday = Golfer(self.golfer_id, self.golfer_name, invalid_bday)
            self.fail()
        except Exception as ex:
            pass

        # negative test case: characters over than slashes and dashes are invalid
        invalid_bday = '04.14.83'
        try:
            arthur_invalid_bday = Golfer(self.golfer_id, self.golfer_name, invalid_bday)
            self.fail()
        except Exception as ex:
            pass





if __name__ == '__main__':
    unittest.main()
