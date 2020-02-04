class Tournament:
    """
    Tournament object derived from data in the tournamentsInput.csv

    Instance variables:
        tourn_id       a unique id for this tournament (to be used as a primary key when stored in the database)
        tourn_name     the name for the tournament
        course_id      the id of the golf course where the tournament was played
        start_date     the date of the first round of this tournament
                       NOTE: tournamentsInput.csv has this field in the format 'm-dd-yy',
                             but the database expects it in the format 'YYYY-mm-dd',
                             so it needs converted

        num_rounds     number of rounds for this tournament (2, 3, or 4)
        num_golfers     number of golfers that played in the tournament

    """
    ### Please provide your definition here from Project 1-B
