from db_util.db import do_command, do_insert


def get_owner_id_by_name(owner_name):
    rslt = do_command(
        "select owner_id from owner where owner_name = ?",
        [owner_name])
    if len(rslt) > 0:
        return rslt[0]['owner_id']
    else:
        return None


def get_owner_id_for_ticket(ticket):
    rslt = do_command(
        '''select owner
            from ticket
            where ticket.value = ?
        ''',
        [ticket]
    )
    if len(rslt) > 0:
        return rslt[0]['owner']
    else:
        return None


def get_loan_ids_for_owner(owner_id):
    rslt = do_command(
        'select loan_id from loan where owner = ?',
        [owner_id]
    )
    return rslt


def get_loan_for_loan_id(loan_id):
    rslt = do_command(
        'select * from loan where loan_id = ?',
        [loan_id]
    )
    if len(rslt) > 0:
        return rslt[0]
    else:
        return None


def owner_is_active(owner_name):
    rslt = do_command(
        'select active from owner where owner_name = ?',
        [owner_name]
    )
    if len(rslt) > 0:
        return rslt[0]['active'] != 0
    else:
        return False


def create_owner(owner_name):
    owner_cmd = """
        insert into owner (owner_name)
        values (?)
    """
    try:
        rtval = do_insert(owner_cmd, [owner_name])
        return rtval
    except:
        return None


def create_loan(owner_id, initial_balance, annual_rate, number_of_months, monthly_payment):
    loan_cmd = """
        insert into loan (owner, initial_balance,
                          annual_rate, number_of_months,
                          monthly_payment)
        values (?,?,?,?,?)
    """
    try:
        rtval = do_insert(loan_cmd, [owner_id, initial_balance, annual_rate, number_of_months, monthly_payment])
        return rtval
    except:
        return None
