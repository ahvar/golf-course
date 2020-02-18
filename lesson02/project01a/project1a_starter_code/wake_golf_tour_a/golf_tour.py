import csv
import pprint
from golfCourse import GolfCourse
from hole import Hole
from golfer import Golfer
from tournament import Tournament


def main():
    """
    1.  Initialize the input and output file names
    2.  Initialize the database and table names for output
    3.  Call create_golf_courses function, passing in the the input
        file name, and retrieving the returned golf_course_list,
        a list of GolfCourse objects containing information for 5 
        golf courses and the returned golf_course_holes_dict which 
        has the golf_course_id as the key, and the value is a list 
        of 18 tuples containing (hole_num, par_value).
    4.  Call create_holes function, passing in the 
        golf_course_holes_dict and retrieving the returned 
        holes_list, a list of Hole objects containing information 
        for 90 (5*18) golf course holes
    5.  Call create_golfers function, passing in the input file name, 
        and retrieving the returned golfer_list, a list of Golfer 
        objects containing information for 30 golfers
    6.  Write out the class objects to files from:
        create_golf_courses, create_holes, create_golfers
     """
    print("Wake Golf Tour Project 1")

    # 1. Initialize the input and output file names

    golf_courses_infile = "golfCoursesInput.csv"
    golfers_infile = "golfersInput.csv"

    golf_courses_file = "golfCourses.csv"
    holes_file = "holes.csv"
    golfers_file = "golfers.csv"


    # 2. Initialize the database and table names for output

    golf_courses_table = "GolfCourse"
    holes_table = "Hole"
    golfers_table = "Golfer"

    # 3. Call create_golf_courses function, passing in the input
    #    file name, and retrieving the returned golf_courses_list,
    #    a list of 5 golf course objects and the golf_course_holes_dict,
    #    containing information about the holes for each of the golf courses

    golf_course_list, golf_course_holes_dict = create_golf_courses(golf_courses_infile)

    # 4. Call create_holes function, passing in the golf_course_holes_dict
    #    and retrieving the returned holes_list, a list of Hole objects 
    #    containing information for 90 golf course holes

    holes_list = create_holes(golf_course_holes_dict)

    # 5. Call create_golfers function, passing in the input
    #    file name, and retrieving the returned golfer_list, 
    #    a list of 30 golfer objects

    golfer_list = create_golfers(golfers_infile)

    # 6. Write out the lists returned from the create functions:
    #    create_golf_courses, create_golfers, create_tournaments

    write_objs_to_file(golf_courses_file, golf_course_list)
    write_objs_to_file(holes_file, holes_list)
    write_objs_to_file(golfers_file, golfer_list)


def create_golf_courses(filename):
    """
    Each line of input contains:
    golf_course_name, par_h1, par_h2, ..., par_h18

    where golf_course_name is the name of the golf course and each
          par_h# is a par value for the hole #.
    
    Note: string input needs to be stripped of any whitespace
             integer strings need to be changed to ints 

    Create a new GolfCourse object containing 
        golf_course_id, golf_course_name, total_par
          
    Return a list, where each element is a GolfCourse object
    """

    print("\nGolf Course List: golf_course_list\n")

    golf_course_list = []
    
    golf_course_holes_dict = dict()

    golf_course_id = 1

    try:
        with open(filename, 'r') as courses_in:
            file_lines = csv.reader(courses_in)
            for course_name, *pars in file_lines:
                holes = []
                hole_count = 1
                for par in pars:
                    total_par = total_par + int(par)
                    holes.append((hole_count, int(par)))
                    hole_count += 1

                golf_course_holes_dict[golf_course_id] = holes

            golf_course_list.append(GolfCourse(golf_course_id, course_name.strip(), total_par))

            golf_course_id += 1

    except IOError:
        print("File Not Found Error.")

    # 5. Print the golf_course_list objects to the console

    for gc in golf_course_list:
        print(gc)

    # 6. Return the golf_course_list and golf_course_holes_dict

    return golf_course_list, golf_course_holes_dict

    
def create_holes(golf_course_holes_dict):
    """
    Use the dictionary created in the create_golf_courses function
    to create a list of Hole objects. The dictionary has golf_course_id as the key,
    and a list of 18 tuples containing (hole_num, par_value) as the value
        Each entry will have:
         golf_course_id: [(hole_num, par_value), 
                          (hole_num, par_value), ..., 
                          (hole_num, par_value)]
                                 
    Create a Hole object for each hole_num and par_value
    containing - 
        hole_id, golf_course_id, hole_num, and par_value

    Return a list,  where each element is a Hole object
                                 
    """
    print("\nThe Hole object list:\n")
    
    #  Create an empty list called holes_list 
    holes_list = [ ]
    # unique id that identifies
    unique_hole_num = 1
    #hole_num_string = 'unique_hole_id'
    #hole_id = f'{hole_num_string}_{unique_hole_num}'

    ### Please provide your code here
    for gc_id, all_holes in golf_course_holes_dict.items():
        for hole in all_holes:
            holes_list.append(Hole(unique_hole_num, gc_id, hole, hole[1]))
            unique_hole_num += 1
            # hole_id = f'{hole_num_string}_{unique_hole_num}'

    # print holes
    for hole in holes_list:
        pprint.pprint(str(hole))

    # return the list
    return holes_list
    

def create_golfers(filename):
    """
    Each line of input contains:
        golfer_name, golfer_birthdate

        where golfer_name is the name of the golfer and
                  golfer_birthdate is the date the golfer was born.

    Note: string input needs to be stripped of any whitespace

    Create a Golfer object from each line in the input file:
    containing - 
        golfer_id, golfer_name, golfer_birthdate

    Return a list,  where each element is a Golfer object
    """
    print ("\nThe Golfer object list:\n")
    
    # Create an empty list called golfer_list
    golfer_list = []
    golfer_num = 1
    with open('golfersInput.csv') as golfers_in:
        g_reader = csv.reader(golfers_in)
        for row in g_reader:
            name, birthdate = row
            no_ltspace_name = name.strip()
            no_ltspace_bday = birthdate.strip()
            #unique_golfer = f'{no_ltspace_name.replace(" ", "_").lower()}_{golfer_num}'
            golfer_list.append(Golfer(golfer_num, no_ltspace_name, no_ltspace_bday))
            golfer_num += 1

    # reset the golfer id
    golfer_num = 1

    # print the golfers to the console
    for golfer in golfer_list:
        pprint.pprint(str(golfer))

    # return the golfer list
    return golfer_list


def create_rounds(tournament_list):
    """
    Use the tournament_list object list, that was
    returned from the create_tournaments function, which
    contains 15 Tournament objects with the following
    instance variables:

    tourn_id, tourn_name, golf_course_id, start_date,
    num_rounds, num_golfers, golfers...

    Create num_rounds Round objects from every
    Tournament object element in tournament_list:
    Add in the following as instance variables values

    round_id, tourn_id, day

    A list is returned, where each element is a Round object
    """
    print("\nThe Round object list\n")
    rounds_list = []

    ### Please provide your code here

    return rounds_list


def create_tournaments(filename, golf_course_list):
    """
    The tournamentsInput.csv has two different record types in the file.
    Hint: Open the file and see how it is organized.
    The first record type has

    golf_course_name, tourn_name, start_date, num_rounds, num_golfers

    where golf_course_name is the name of the golf course,
          tourn_name is the name of the tournament,
          start_date is the first day of the tournament,
          num_rounds is the number of rounds played in this tournament, and
          num_golfers is the number of golfers playing in this tournament

    The second record type is just a single golfer name.
    The number of these records is specified by the num_golfers field from the first record type
        golfer1_name
        golfer2_name
        ...
        golfer15_name

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Create a Tournament object
    containing -
        golfer_id, golfer_name, golfer_birthdate

    Create dictionary entry value for this tourn_id_key,
        the value is a list to be filled in with the golfer names
        as they are read from the input file.

    Return the tournament_list and tourn_golfers_dict
    """
    print("\nThe Tournament object list:\n")

    # Create an empty list called tournament_list
    tournament_list = []

    # Create an empty dictionary called tourn_golfers_dict
    tourn_golfers_dict = dict()
    with open('tournamentsInput.csv', 'r') as tourn_in:
        tourn_reader = csv.reader(tourn_in)
        tourn_data = list(tourn_reader)

    tourn_id = 1
    for entry in tourn_data:
        if entry[0].find('Golf Course') is not -1:
            tourn_name, course_id, date_str, num_rounds, num_golfers = entry
            t = Tournament(tourn_id, tourn_name, course_id, date_str, num_rounds, num_golfers)
            start = tourn_data.index(entry) + 1
            end = start + int(num_golfers)
            tourn_golfers_dict[t] = tourn_data[start:end]
            tournament_list.append(t)
            tourn_id += 1

    return tournament_list, tourn_golfers_dict


def create_tourn_golfers(tourn_golfers_dict, golfer_list):
    """
    Use the tourn_golfers_dict, that was
    returned from the create_tournaments function, which contains
    entries with the key being the tourn_id, and the value is a list of golfer_names

    Use the golfers_list object list parameter, that was returned from the
    create_golfers function, which contains 30 Golfer objects with
    the following instance  variables:

        golfer_id, golfer_name, golfer_birthdate

    Create a TournGolfer object from every golfer_name listed
    in the tourn_golfers_dict.
    Add in the following as instance variables values -

        tourn_golfer_id, tourn_id, golfer_id

    A list is returned, where each element is a TournGolfer object

    """

    print("\nThe TournGolfer object list\n")
    tourn_golfers_list = []

    ### Please provide your code here

    return tourn_golfers_list


def write_objs_to_file(filename, object_list):
    """
    This function takes a nested_list as input and writes it
    out to the specified csv file, where each line is a inner list
    """
    
    # 1. Open the output file object for writing

    output_file = open(filename, 'w')

    # 2. Create a loop to traverse the object_list parameter,
    #    where the loop variable is each object in the list:

    for obj in object_list:
        # Loop:
        # a. Set a str_obj string variable to the result of
        #    converting 'object' to a string using the
        #    __str__ method of the output file.  This can be
        #    accomplished by passing the object into the
        #    str() function.

        str_obj = str(obj)

        # b. Add a new line character to the end of the
        #     str_obj string

        str_obj += '\n'

        # c. Use the write method of the output file object
        #    to write the str_obj string to the output file,

        output_file.write(str_obj)

    # 3. Close the output file

    output_file.close()


if __name__ == "__main__":
    main()
