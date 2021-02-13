import sqlite3
from sqlite3 import Error


# need to create a db connection
def create_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# where i defined the path to the database
if __name__ == '__main__':
    create_db(r"C:\Users\heath\PycharmProjects\final\commands\Courses.db")