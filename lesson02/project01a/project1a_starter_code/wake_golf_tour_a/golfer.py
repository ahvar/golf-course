import datetime
import re
import string
import lesson02.project01a.project1a_starter_code.wake_golf_tour_a.golfer_utilities as utilities


class Golfer:
    """Golfer object derived from data in the golfersInput.csv

    Attributes:
        golfer_id          a unique id for this golfer (to be used as a primary key when stored in the database)
        golfer_name        the name for the golfer
        golfer_birthdate   the golfers birthdate
                           NOTE: golfersInput.csv has this field in the format 'mm-dd-yy',
                                 but the database expects it in the format 'YYYY-mm-dd', so it needs converted

    """

    def __init__(self, golfer_id=None, name=None, bday=None):
        """
        constructor of class Hole (typo? this is the Golfer class)
        """
        self._golfer_id = None
        self._golfer_name = None
        self._golfer_birthdate = None
        self.golfer_birthdate = bday
        self.golfer_id = golfer_id
        self.golfer_name = name
    
    ### Please complete the following functions
    
    # get_golfer_id
    @property
    def golfer_id(self) -> str:
        """
        return the golfer_id to the caller
        """
        return self._golfer_id

    @golfer_id.setter
    def golfer_id(self, id):
        """
        Sets the golfer id. Only letters and digits can comprise the golfer id
        :param id: unique golfer id
        :return:
        """
        if not utilities.valid_id(id):
            raise Exception('Only letters and digits can comprise the golfer id')
        self._golfer_id = id

    # get_golfer_name
    @property
    def golfer_name(self) -> str:
        """
        return the golfer_name to the caller
        """
        return self._golfer_name

    @golfer_name.setter
    def golfer_name(self, name):
        """
        Sets the golfer name to the name parameter. Only letters can comprise a Golfer's name.
        :param name:
        :return:
        """
        digits = [digit for digit in string.digits if name.find(digit) is not -1]
        if len(digits) > 0:
            raise Exception("Only letters can comprise the golfer name")
        self._golfer_name = name
    
    # get_golfer_birthdate
    @property
    def golfer_birthdate(self) -> str:
        """
        return the golfer_birthdate to the caller
        """
        return self._golfer_birthdate

    @golfer_birthdate.setter
    def golfer_birthdate(self, bday):
        self._golfer_birthdate = utilities.to_sql_date(bday)

    # __str__
    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        return f'{self.golfer_id},{self.golfer_name},{self.golfer_birthdate}'

    def __repr__(self):
        """
        Return the code representation of an instance of Golfer
        :return:
        """

    def __format__(self, code):
        """

        :param code:
        :return:
        """