import unittest
import os
import time
from lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfer import Golfer
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfer_utilities as utilities


class TestUtilities(unittest.TestCase):
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
        # cls._golfer_abs_path = os.path.join(cls._current_directory, "golfer.py")

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
        try:
            self.arthur = Golfer(self.golfer_id, self.golfer_name, self.golfer_bday)
        except Exception as ex:
            self.fail('Could not construct golfer')
        # the birthday format is not valid
        # arthur_invalid_bday = Golfer(golfer_id, golfer_name, "04 14 83")
        # the name is invalid
        # arthur_invalid_name = Golfer(golfer_id, "Ar$thur Vargas", "04-14-83")

    @classmethod
    def tearDownClass(cls):
        os.chdir(cls._current_directory)

    def print_output(self, ret, out, err):
        """
        Print the stdout and stderr values that have been captured
        :param ret: return code
        :param out: stdout
        :param err: stderr
        :return:
        """
        print("\n***********************************************************************************")
        print("Return the value: %s" % ret)
        print("\n***********************************************************************************")
        print("Length of stdout: %s" % len(out))
        print("stdout:")
        print(out.decode())
        print("\n***********************************************************************************")
        print("Length of stderr: %s" % len(err))
        print("stderr:")
        print(err.decode())

    def create_test_case_output_dir_and_cd(self, dir_name):
        """
        Create a subdirectory to hold the results of this test
        :param dir_name: directory name
        :return:
        """
        os.makedirs(dir_name)
        print("Output directory for this test = {}".format(dir_name))
        os.chdir(dir_name)
        self._testcase_dir_path = os.path.join(self._output_path, dir_name)
        print("self._testcase_dir_path = {}".format(dir_name))

    def test_to_sql_date(self):
        print("\n\n____________________________________________________________")
        print("Test Case: nominal, test the conversion of the date to the sql date format")
        test_output_dir = "test_to_sql_date"
        self.create_test_case_output_dir_and_cd(test_output_dir)

        # positive test case: golfer arthur was constructed during setup
        try:
            self.assertEqual(str(self.arthur), '1,Arthur Vargas,1983-04-14')
        except Exception as ex:
            self.fail(f'An {ex} was thrown when it should not have been')

        # positive test case: a bday with foward slashes and a four digit year
        try:
            carlo = Golfer(2, "Carlo Vargas", "12/08/1984")
            self.assertEqual(str(carlo), '2,Carlo Vargas,1984-12-08')
        except Exception as ex:
            self.fail(f'An {ex} was thrown when constructing a golfer with a four digit year bday with slashes')

        # positive test case: a bday with forward slashes and a two digit year
        try:
            anna = Golfer(3, "Anna Maria Vargas", "10/28/89")
            self.assertEqual(str(anna), '3,Anna Maria Vargas,1989-10-28')
        except Exception as ex:
            self.fail(f'An {ex} was thrown when constructing a golfer with a two digit year bday with forward slashes')

        # negative test case: whitespace is an invalid separator
        invalid_bday = '04 14 83'
        try:
            chris = Golfer(4, "Christopher Maglione", invalid_bday)
            self.fail()
        except Exception as ex:
            pass

        # negative test case: characters over than slashes and dashes are invalid
        invalid_bday = '08.14.85'
        try:
            topher = Golfer(5, "Christopher Maglione", invalid_bday)
            self.fail()
        except Exception as ex:
            pass


        ###############################################################################################################
        # TESTING ALTERNATE DATE CONVERSION IMPLEMENTATIONS
        ###############################################################################################################

        # positive test case with all combinations of valid date format code
        d = utilities.Date(1983, 4, 14)
        holly_bday = utilities.Date(1988, 2, 1)
        carlo_bday = utilities.Date(1984, 12, 8)
        papa_bday = utilities.Date(1947, 5, 28)
        try:
            self.assertEqual(format(d), '1983-4-14')
            self.assertEqual(format(holly_bday), '1988-2-1')
            self.assertEqual(format(d, 'ymd'), '1983-4-14')
            self.assertEqual('the date is {:ymd}'.format(d), 'the date is 1983-4-14')
            self.assertEqual('the date is {:mdy}'.format(d), 'the date is 4/14/1983')
            self.assertEqual('the date is {:dmy}'.format(d), 'the date is 14/4/1983')
        except Exception as ex:
            self.fail(ex)

        # negative test case with digits in the date format code
        try:
            arthur = utilities.Date(1983, 4, 14)
            self.assertEqual(format(arthur, 'm4y'), '1983/4/14')
            self.fail()
        except Exception as ex:
            self.assertEqual(str(ex), "code must only be comprised with 'm', 'y', 'd' ")

        # negative test case with whitespace in the format code
        try:
            anna = utilities.Date(1988, 10, 28)
            self.assertEqual("anna's birthday is {:y md}".format(anna), "anna's birthday is 1988-10-28")
            self.fail()
        except Exception as ex:
            self.assertEqual(str(ex), "code contains whitespace characters. only 'm', 'y', 'd' are allowed")


if __name__ == '__main__':
    unittest.main()
