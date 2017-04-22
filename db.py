import csv

def welcome():
    print('Welcome to the User database, \n ')
    welcome = input('Please choose (L)og in or (C)reate a user').lower()
    if welcome == "l":
        return log_in_db()
    elif welcome == "c":
        return new_user()


def new_user():

    user_name = input("enter user ")
    password = input("enter password ")
    name = input("Enter your name ")
    added_data = input("Enter new data ")
    line = "{},{},{},{}\n".format(user_name, password, name, added_data)

    with open("db_a.csv","a") as outfile:
        outfile.write(line)


def search_db():

    with open("db_a.csv","r") as infile:
        data = csv.DictReader(infile,fieldnames=['user_name', 'password', 'name', 'added_data'])
        for row in data:
            print(row['password'])


def log_in_db():
    user_is = input('enter user_name  ')
    password = input('enter password  ')

    with open("db_a.csv", "r") as infile:
        data = csv.DictReader(infile, fieldnames=['user_name', 'password', 'name', 'added_data'])
        for row in data:
            if user_is == row['user_name'] and password == row['password']:
                print('success you are logged in')

                logged_in = input('(r)ead your data')
                if logged_in == 'r':
                    print(row['added_data'])

            elif user_is != row['user_name'] and password == row['password']:
                print('Please retry log in')
                return log_in_db()
            elif user_is == row['user_name'] and password != row['password']:
                print('Please retry logging in')
                return log_in_db()
        else:
            return log_out()


def log_out():
    log_out = input('Please select(R)eturn to go back to login screen:,\n To(Q)uit to end program, \n Or choose any other key to create a new user' ).lower()
    if log_out == "r":
        return log_in_db()
    elif log_out == "q":
        return exit()
    else:
        return new_user()













welcome()
log_in_db()
search_db()
log_out()
