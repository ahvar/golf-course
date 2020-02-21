import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfer_utilities as utilities
#import golfer_utilities as utilities


class Hole:
    """
    Hole object derived from data in the golfCoursesInput.csv

    Attributes:
        hole_id:   a unique id for this hole (to be used as a primary key when stored in the database)
        course_id: the id of the golf course where this hole is played
        hole_num:  the number of the hole (1-18)
        par:       the par value for this hole (3,4, or 5)
    """

    ### Please complete the following functions
    
    # __init__
    def __init__(self, hole_id: str, course_id: str, hole_num: int, par: int):
        """
        constructor of class Hole
        """
        # unique id for this hole
        self._hole_id = hole_id
        # unique id for this course
        self._course_id = course_id
        # unique int for this hole
        self._hole_num = hole_num
        # the par for this hole
        self._par = par
        self.hold_id = None
        self.course_id = None
        self.hole_num = None
        self.par = None

    # get_hole_id
    @property
    def hole_id(self):
        """
        return the hole_id to the caller
        """
        return self._hole_id

    @hole_id.setter
    def hole_id(self, id):
        if not utilities.valid_id(id):
            raise Exception(utilities.INVALID_ID.format("hole_id"))
        self._hole_id = id

    # get_course_id
    @property
    def course_id(self):
        """
        return the course_id to the caller
        """
        return self._course_id

    @course_id.setter
    def course_id(self, id):
        if not utilities.valid_id(id):
            raise Exception(utilities.INVALID_ID.format("course_id"))
        self._course_id = id

    # get_hole_num
    @property
    def hole_num(self):
        """
        return the hole_num to the caller
        """
        return self._hole_num

    @hole_num.setter
    def hole_num(self, num):
        if num < 1 or num > 18:
            raise Exception("Hole number must be 1 - 18")
        self._hole_num = num

    # get_par
    @property
    def par(self):
        """
        return the hole par to the caller
        """
        return self._par

    @par.setter
    def par(self, par):
        self._par = par

    # __str__
    def __str__(self):
        """
        create a comma-delimiter string
        of the instance variable values
        """
        return f'{self.hole_id, self.course_id, self.hole_num, self.par}'
