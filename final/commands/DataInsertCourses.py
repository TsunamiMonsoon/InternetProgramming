# this is similar to the file add_data.py but tweaked a bit to work

import sqlite3
from sqlite3 import Error


def create_db(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connect = None
    try:
        connect = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connect


# function that will create the courses table after getting courses info
def create_courses(conn, courses):
    """
   Create a new course
    :param conn:
    :param courses:
    :return:
    """

    sqlite = ''' INSERT INTO courses(course_id, department, course_number,course_name ,semester ,year ,grade)
              VALUES(?,?,?,?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sqlite, courses)
    return cursor.lastrowid


# function that will create the prereq table after getting the defined values
def create_prereqs(conn, prereqs):
    """
   Create a new table for prereqs
    :param conn:
    :param prereqs:
    :return:
    """
    sqlite = ''' INSERT INTO prereq(course_id, prereq1, prereq2)
              VALUES(?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sqlite, prereqs)
    return cursor.lastrowid


# define the courses and prereq information here then establish the tables with given info through connection
def main():
    database = r"C:\Users\heath\PycharmProjects\final\commands\Courses.db"

    # create the connection to the database
    connect = create_db(database)
    with connect:
        # courses
        course_1 = (1, 'MATH', '1190', 'Calculus I', 'Summer', '2018', 'A')
        course_2 = (2, 'CSE', '1322', 'Programming and Problem Solving', 'Fall', '2018', 'B')
        course_3 = (3, 'CSE', '1322L', 'Programming and Problem Solving Lab', 'Fall', '2018', 'C')
        course_4 = (4, 'CS', '3305', 'Data Structures', 'Spring', '2019', 'A')
        course_5 = (5, 'CS', '3503', 'Computer Organization and Architecture', 'Spring', '2019', 'B')
        course_6 = (6, 'MATH', '2202', 'Calculus II', 'Spring', '2019', 'C')
        course_7 = (7, 'MATH', '2345', 'Discrete Mathematics', 'Fall', '2018', 'A')
        course_8 = (8, 'CS', '3410', 'Introduction to Database Systems', 'Spring', '2020', 'B')
        course_9 = (9, 'SWE', '3313', 'Introduction to Software Engineering', 'Spring', '2020', 'C')
        course_10 = (10, 'CSE', '3801', 'Professional Practices and Ethics', 'Spring', '2020', 'A')

        # here we create courses
        create_courses(connect, course_1)
        create_courses(connect, course_2)
        create_courses(connect, course_3)
        create_courses(connect, course_4)
        create_courses(connect, course_5)
        create_courses(connect, course_6)
        create_courses(connect, course_7)
        create_courses(connect, course_8)
        create_courses(connect, course_9)
        create_courses(connect, course_10)

        # prereqs here
        prereq1 = (1, 0, 0)
        prereq2 = (2, 0, 0)
        prereq3 = (3, 0, 0)
        prereq4 = (4, 2, 3)
        prereq5 = (5, 2, 3)
        prereq6 = (6, 1, 0)
        prereq7 = (7, 0, 0)
        prereq8 = (8, 2, 3)
        prereq9 = (9, 2, 3)
        prereq10 = (10, 2, 3)

        # create the prereqs now
        create_prereqs(connect, prereq1)
        create_prereqs(connect, prereq2)
        create_prereqs(connect, prereq3)
        create_prereqs(connect, prereq4)
        create_prereqs(connect, prereq5)
        create_prereqs(connect, prereq6)
        create_prereqs(connect, prereq7)
        create_prereqs(connect, prereq8)
        create_prereqs(connect, prereq9)
        create_prereqs(connect, prereq10)


if __name__ == '__main__':
    main()
