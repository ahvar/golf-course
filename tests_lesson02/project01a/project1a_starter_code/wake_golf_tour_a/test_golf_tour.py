import unittest
import os
import time
import pprint
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfer_utilities as golfer_utilities
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfCourse as golfCourse
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.hole as hole
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfer as golfer
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.tournament as tournament
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golf_tour as golf_tour


class TestGolfTour(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        This method can be used to define fields which will be used throughout the test class.
        :return:
        """
        # Save the current directory so we know the path to the source.  This is used for running the program through
        # the command line. It's also used to reset the current working directory after a test completes.
        cls._current_directory = os.getcwd()
        cls._golf_tour_abs_path = os.path.join(cls._current_directory, "golf_tour.py")
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
        self.golf_courses_infile = \
            "/rhome/q1016330/dev/scrap/golf-course/tests_lesson02/project01a/project1a_starter_code/wake_golf_tour_a/golf_course.csv"
        #self.golfers_infile = "golfersInput.csv"

        #self.golf_courses_file = "golfCourses.csv"
        #self.holes_file = "holes.csv"
        #self.golfers_file = "golfers.csv"

    @classmethod
    def tearDownclass(cls):
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

    def test_create_golf_courses(self):
        print("\n\n__________________________________________________________________________________________")
        print("Test Case: nominal, test reading in golf course data")
        testcase_output_dir = "test_create_golf_courses"
        self.create_test_case_output_dir_and_cd(testcase_output_dir)

        try:
            golf_course_list, golf_course_holes_dict = golf_tour.create_golf_courses(self.golf_courses_infile)
            raleigh_gc = [4, 3, 4, 4, 4, 5, 4, 4, 4, 4, 3, 4, 4, 4, 5, 4, 4, 4]
            wtcc_gc = [4, 4, 3, 4, 4, 4, 5, 4, 4, 4, 4, 3, 4, 4, 4, 5, 4, 4]
            garner_gc = [4, 4, 4, 4, 5, 4, 4, 4, 3, 4, 4, 4, 5, 4, 4, 4, 3, 4]
            cary_gc = [4, 4, 4, 4, 3, 4, 5, 4, 4, 5, 4, 4, 4, 3, 4, 4, 4, 4]
            apex_gc = [4, 4, 4, 5, 4, 4, 3, 4, 4, 4, 5, 4, 4, 4, 3, 4, 4, 4]
            if not TestGolfTour.verify_gc_par_list(golf_course_holes_dict[1], raleigh_gc) \
                    or not TestGolfTour.verify_gc_par_list(golf_course_holes_dict[2], wtcc_gc) \
                    or not TestGolfTour.verify_gc_par_list(golf_course_holes_dict[3], garner_gc) \
                    or not TestGolfTour.verify_gc_par_list(golf_course_holes_dict[4], cary_gc) \
                    or not TestGolfTour.verify_gc_par_list(golf_course_holes_dict[5], apex_gc):
                self.fail()

        except Exception as ex:
            print(ex)
            self.fail()

    @staticmethod
    def verify_gc_par_list(list_of_tuples, list_of_pars) -> bool:
        """
        Every index of the list of tuples is a tuple with the hole (1 - 18) and the par for that hole. We assume
        that the holes are organized in ascending order. we also assume that the correct list of pars has been passed,
        otherwise the test will fail as the wrong list of pars has been passed.

        :param list_of_tuples: a list of tuples containing the hole number and the par for that hole
        :param list_of_pars: a list of actual pars for a course
        :return:
        """
        for i in range(1, 18):
            hole_par = tuple(list_of_tuples[i - 1])
            if hole_par[0] is not i or hole_par[1] is not list_of_pars[i - 1]:
                return False
        return True


    def test_create_holes(self):
        pass

    def test_create_golfers(self):
        pass


if __name__ == '__main__':
    unittest.main()
