import sqlite3
from os.path import join, split


# get a path to the database file "sqlite-sakia.sq"
# print(__file__)
# dirname = split(__file__)[0]
#
# print(filepath)

def dictionary_factory(cursor, row):
    """
    create a dictionary from rows in a cursor result
    the keys will be the column names
    :param cursor: a cursor from which a query row has just been fetched
    :param row: The query row that was fetched
    :return: A dictionary associating column names to values
    """
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))


def getConnection():
    this_dir = split(__file__)[0]
    fname = join(this_dir, 'sqlite-sakila.sq')
    conn = sqlite3.connect(fname)
    conn.row_factory = dictionary_factory  # note: no parenthesesreturn conn
    conn .row_factory = dictionary_factory
    return conn


#conn = getConnection()
#cur = conn.cursor()
#cmd = "select * from customer"
#cur.execute(cmd)
#customer = cur.fetchall()
#print(cur.description)


def do_command(cmd, args=[]):
    try:
        conn = getConnection()
        crs = conn.cursor()
        crs.execute(cmd, args)
        return crs.fetchall()
    finally:
        conn.close()
# conn = sqlite3.connect("sqlite-sakila.sq")

# create a query
# cmd = "select * from customer"


# create a cursor
# crs = conn.cursor()

# send a query and receive query result
# crs.execute(cmd)

# customer = crs.fetchall()

# for row in customer:
#       print(row)

# print("=" * 100)

# for row in customer:
#    print(row)
