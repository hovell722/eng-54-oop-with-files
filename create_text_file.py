from new_users_class import *


def create_new_users(file):
    try:
        with open(file + '.txt', 'w') as filed:
            count = 0
            while count < 10:
                count += 1
                name = input("Input a name: ")
                new_user = NewUsers(name)
                filed.write(str(new_user.name) + '\n')
    except FileNotFoundError as error:
        print(error)
    finally:
        print("Finished writing program")
