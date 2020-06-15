from Database.db import do_command
from Database.Db_access import *

cmd = list_of_all_stores()

for row in cmd:
    print(row)