import unittest
import os
import time
from lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfer import Golfer


class TestGolfer(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
