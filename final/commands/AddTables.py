import sqlite3
from sqlite3 import Error


def create_db(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# function that defines the tables and creates them
def main():
    database = r"C:\Users\heath\PycharmProjects\final\commands\Courses.db"

    sql_create_courses_table = """ CREATE TABLE IF NOT EXISTS courses (
                                        course_id integer PRIMARY KEY,
                                        department text NOT NULL,
                                        course_number integer NOT NULL,
                                        course_name text NOT NULL,
                                        semester text NOT NULL,
                                        year integer NOT NULL,
                                        grade text NOT NULL
                                    ); """

    sql_create_prereq_table = """CREATE TABLE IF NOT EXISTS prereq(
                                    course_id integer PRIMARY KEY,
                                    prereq1 integer NOT NULL,
                                    prereq2 integer NOT NULL,
                                    FOREIGN KEY(course_id) REFERENCES courses (course_id)
                                );"""

    # create a database connection
    conn = create_db(database)

    # create tables
    if conn is not None:
        # create courses table
        create_table(conn, sql_create_courses_table)

        # create prereq table
        create_table(conn, sql_create_prereq_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()