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
        self.__round_id = round_id
        # unique id for this tournament
        self.__tourn_id = tourn_id
        # unique int for this hole
        self.__day = day

    # get_hole_id
    def get_round_id(self):
        """
        return the round_id to the caller
        """
        return self.__round_id

    # get_course_id
    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    # get_hole_num
    def get_day(self):
        """
        return the day to the caller
        """
        return self.__day

    # __str__
    def __str__(self):
        """
        create a comma-delimiter string
        of the instance variable values
        """
        return f'{self.get_round_id(), self.get_tourn_id(), self.get_day()}'


