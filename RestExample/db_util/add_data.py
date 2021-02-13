
from db import do_command

from loans import computeMonthlyPayment

do_command("delete from owner")
do_command("delete from loan")


owners = ["Alice", "Bob", "Charles", "Dora", "Eve", "Frank"]
owner_cmd = """
    insert into owner (owner_name)
    values (?)
"""
for x in owners:
    do_command(owner_cmd, [x])

loan_list = [
    [10000, .1, 20],
    [5000, .05, 30],
    [30000, .08, 10],
]
loan_cmd = """
    insert into loan (owner, initial_balance,
                      annual_rate, number_of_months,
                      monthly_payment)
    values (?,?,?,?,?)
"""


for ow in owners:
    rslt = do_command(
        "select owner_id from owner where owner_name = ?",
        [ow])
    oid = rslt[0]['owner_id']
    # print(oid)
    for ln in loan_list:
        bal = ln[0]
        ar = ln[1]
        nm = ln[2]
        paymt = computeMonthlyPayment(bal, ar, nm)
        do_command(loan_cmd,
                   [oid, bal, ar, nm, paymt])

