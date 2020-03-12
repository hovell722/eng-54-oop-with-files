from new_users_class import *

def read_new_users(file):
    try:
        with open(file + '.txt', 'r') as file:
            user_list = file.readlines()
            for user in user_list:
                print(user.strip('\n'))
    except FileNotFoundError as error:
        print(error)
    finally:
        print("Finished reading program")

read_new_users('test')