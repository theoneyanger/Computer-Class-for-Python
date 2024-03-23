from datetime import datetime
def error(name ,err_type):
    f = open("Logs.txt", 'a+')
    date = datetime.now()
    time = date.strftime('%H:%M:%S')
    f.write(f'AN ERROR OCCURRED IN {name} ON {date}. ERROR NAME: {err_type}.\n')
    f.close()
def logged(name):
    now = datetime.now()
    time = now.strftime('%H:%M:%S')
    date = now.strftime("%d/%m/%Y")
    f = open("Logs.txt", 'a+')
    f.write(f"USER LOGGED IN {name} on date: {date} and time: {time}.\n")
    f.close()
def exited(name):
    now = datetime.now()
    time = now.strftime('%H:%M:%S')
    date = now.strftime("%d/%m/%Y")
    f = open("Logs.txt", 'a+')
    f.write(f"USER CLOSED PROGRAM {name} on date: {date} and time: {time}.\n")