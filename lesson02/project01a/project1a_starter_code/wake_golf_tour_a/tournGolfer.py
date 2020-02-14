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
    def __init__(self, tourn_golfer_id, tourn_id):
        """
        constructor of class Hole (typo? this is the Golfer class)
        """
        # tourn_golfer_id
        self.__tourn_golfer_id = tourn_golfer_id

    ### Please complete the following functions

    # get_golfer_id
    def golfer_id(self) -> str:
        """
        return the golfer_id to the caller
        """
        return self._golfer_id

    # get_golfer_name
    def golfer_name(self) -> str:
        """
        return the golfer_name to the caller
        """
        return self._golfer_name

    # get_golfer_birthdate
    def golfer_birthdate(self) -> str:
        """
        return the golfer_birthdate to the caller
        """
        return self._golfer_birthdate

    # __str__
    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        return f'{self.golfer_id()},{self.golfer_name()},{self.golfer_birthdate()}'