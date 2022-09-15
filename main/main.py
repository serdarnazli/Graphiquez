import screens as sc
import time
import database as db


def databaseConnectScreen():
    while True:

        flag = 0

        try:
            database = db.Database()
            database.connect()
            flag = 1
            return database
        except Exception as f:
            flag = 0
            print(f)
        if flag == 1:
            break
        time.sleep(5)


database = databaseConnectScreen()
screens = sc.Screens(database)

screens.intro()
while True:  # main thing goes on here.
    is_log_succesful = False
    process = screens.start_screen()
    if process == "1":
        database.newAcc()
        continue
    else:
        message, username = screens.log_in_screen()
        if message == "BackScreen":
            continue
        if message == "NoProblem":
            is_log_succesful = True

    if is_log_succesful == True:
        screens.signed_processes(username)