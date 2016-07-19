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
    user_is = input('enter user_name' ' ')
    password = input('enter password'' ')

    with open("db_a.csv", "r") as infile:
        data = csv.DictReader(infile, fieldnames=['user_name', 'password', 'name', 'added_data'])
        for row in data:
            if user_is == row['user_name'] and password == row['password']:
                print('success you are logged in')
            elif user_is != row['user_name'] and password == row['password']:
                print('Please retry log in')
                return log_in_db()
            elif user_is == row['user_name'] and password != row['password']:
                print('Please retry logging in')
                return log_in_db()
        else:
            input('press any key to quit' )
            return exit()







search_db()
log_in_db()