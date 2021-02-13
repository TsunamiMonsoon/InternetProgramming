
from db import do_command, do_command_no_return


def do_drop():
    drop_owner = """drop table if exists owner"""
    do_command(drop_owner)
    drop_loan = """drop table if exists loan"""
    do_command(drop_loan)
    drop_ticket = """drop table if exists ticket"""
    do_command(drop_ticket)



def do_create():
    cmd_owner = """
        create table owner
        (
          owner_id integer PRIMARY KEY autoincrement,
          owner_name varchar(30) UNIQUE ,
          active INTEGER DEFAULT 1
        )
    """
    do_command(cmd_owner)

    cmd_loan = """
        create table loan
        (
          loan_id integer primary key autoincrement,
          owner REFERENCES owner(owner_id),
          initial_balance real,
          number_of_months integer,
          annual_rate real,
          monthly_payment real
        )
    """
    do_command(cmd_loan)

    cmd_ticket = """
        create table ticket (
          owner REFERENCES owner(owner_id),
          value text UNIQUE,
          expires TIMESTAMP
        )
    """
    do_command(cmd_ticket)


if __name__ == "__main__":
    do_drop()
    do_create()
