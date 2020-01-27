import datetime

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
        convert csv date ('mm-dd-yy') to sql date ('YYYY-mm-dd')
        """
        m, d, y = bday.split(sep='-')
        # assuming for now that all golfers born in the 20th century; might change this later
        year = int(y) + 1900
        date = datetime.date(year, int(m), int(d))
        return f'{date.year}-{date.month}-{date.day}'

    # __str__
    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        return f'{self.get_golfer_id()},{self.get_golfer_name()},{self.get_golfer_birthdate()}'
