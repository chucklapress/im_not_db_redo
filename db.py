import csv


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
    log_out = input('Please select(L)og out, to(Q)uit or any other key to create a user' )
    if log_out == "L":
        return log_in_db()
    elif log_out == "Q":
        return exit()
    else:
        return new_user()














log_in_db()
search_db()
log_out()
