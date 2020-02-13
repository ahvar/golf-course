from golfer import Golfer


class TournGolfer(Golfer):
    """
    TournGolfer object derived from data in the tournamentInput.csv

    Instance variables:
        tourn_golfer_id    a unique id for this tourn_golfer (to be used as a primary key when stored in the database)
        tourn_id           the id of the tournament played by the golfer
        golfer_id          the id of the golfer playing in the tournament

    """
    ### Please complete this class
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

    # __str__
    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        return f'{self.get_golfer_id()},{self.get_golfer_name()},{self.get_golfer_birthdate()}'