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
    def __init__(self, golfer_id, golfer_name, golfer_birthday, tourn_golfer_id, tourn_id):
        """
        constructor of class Hole (typo? this is the Golfer class)
        """
        super(Golfer, self).__init__(golfer_id, golfer_name, golfer_birthday)
        # the id for the golfer at the tournament
        self._tourn_golfer_id = tourn_golfer_id
        # the id for this tournament
        self._tourn_id = tourn_id

    ### Please complete the following functions
    @property
    def tourn_golfer_id(self):
        return self._tourn_golfer_id

    @property
    def tourn_id(self):
        return self._tourn_id

    # __str__
    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        return f'{self.golfer_id},{self.golfer_name},{self.golfer_birthdate},{self.tourn_golfer_id},{self._tourn_id}'
