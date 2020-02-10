import datetime
import re

class Golfer:
    """Golfer object derived from data in the golfersInput.csv

    Attributes:
        golfer_id          a unique id for this golfer (to be used as a primary key when stored in the database)
        golfer_name        the name for the golfer
        golfer_birthdate   the golfers birthdate
                           NOTE: golfersInput.csv has this field in the format 'mm-dd-yy',
                                 but the database expects it in the format 'YYYY-mm-dd', so it needs converted

    """

    def __init__(self, golfer_id, name, bday):
        """
        constructor of class Hole (typo? this is the Golfer class)
        """
        # golfer id
        self.__golfer_id = golfer_id
        # golfer name
        self.__golfer_name = name
        # golfer birthdate
        self.__golfer_birthdate = self.to_sql_date(bday)
    
    ### Please complete the following functions
    
    # get_golfer_id
    def get_golfer_id(self) -> str:
        """
        return the golfer_id to the caller
        """
        return self.__golfer_id

    # get_golfer_name
    def get_golfer_name(self) -> str:
        """
        return the golfer_name to the caller
        """
        return self.__golfer_name
    
    # get_golfer_birthdate
    def get_golfer_birthdate(self) -> str:
        """
        return the golfer_birthdate to the caller
        """
        return self.__golfer_birthdate

    # to_SQL_date(self, bday)
    def to_sql_date(self, bday: str) -> str:
        """
        convert csv date to sql date ('YYYY-mm-dd')
        """
        # dd/mm/yyyy
        four_digit_slash_year = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", bday)
        # dd-mm-yyyy
        four_digit_dash_year = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}", bday)
        # dd/mm/yy
        two_digit_slash_year = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{2}", bday)
        # dd-mm-yy
        two_digit_dash_year = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2}", bday)

        if len(four_digit_slash_year) > 0:
            month, day, year = four_digit_slash_year[0].split('/')
            return f'{year}-{month}-{day}'
        elif len(four_digit_dash_year) > 0:
            month, day, year = four_digit_dash_year[0].split('-')
            return f'{year}-{month}-{day}'
        elif len(two_digit_slash_year) > 0:
            month, day, year = two_digit_slash_year[0].split('/')
            century_20_bday = int(year) + 1900
            return f'{century_20_bday}-{month}-{day}'
        elif len(two_digit_dash_year) > 0:
            month, day, year = two_digit_dash_year[0].split('-')
            century_20_bday = int(year) + 1900
            return f'{str(century_20_bday)}-{month}-{day}'
        else:
            raise Exception

    # __str__
    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        return f'{self.get_golfer_id()},{self.get_golfer_name()},{self.get_golfer_birthdate()}'
