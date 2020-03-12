from new_users_class import *
from create_text_file import *
from read_text_file import *

file_name = input("What would you like your file name to be? ")

create_new_users(file_name)

read_new_users(file_name)

user = NewUsers('James')

user.information(file_name)

