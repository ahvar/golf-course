import golfer_utilities as utilities


class Round:
    """
    Round object derived from data in the tournamentInput.csv

    Instance variables:
        round_id        a unique id for this round (to be used as a primary key when stored in the database)
        tourn_id        the id of the tournament for this round
        day             the day that the round was played ('Thu', 'Fri', 'Sat', 'Sun')
    """
    ### Please complete this class
    # __init__
    def __init__(self, round_id: int, tourn_id: int, day: str):
        """
        constructor of class Round
        """
        # unique id for this round
        self._round_id = round_id
        # unique id for this tournament
        self._tourn_id = tourn_id
        # unique int for this hole
        self._day = day
        self.round_id = None
        self.tourn_id = None
        self.day = None

    # get_hole_id
    @property
    def round_id(self):
        """
        return the round_id to the caller
        """
        return self._round_id

    @round_id.setter
    def round_id(self, id):
        if not utilities.valid_id(id):
            raise Exception(utilities.INVALID_ID.format("round_id"))
        self._round_id = id

    @property
    def tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self._tourn_id

    @tourn_id.setter
    def tourn_id(self, id):
        if not utilities.valid_id(id):
            raise Exception(utilities.INVALID_ID.format("tourn_id"))
        self._tourn_id = id

    @property
    def day(self):
        """
        return the day to the caller
        """
        return self._day

    @day.setter
    def day(self, day):
        self._day = day

    # __str__
    def __str__(self):
        """
        create a comma-delimiter string
        of the instance variable values
        """
        return f'{self.round_id, self.tourn_id, self.day}'


