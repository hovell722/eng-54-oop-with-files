
class NewUsers():
    def __init__(self, name):
        self.name = name

    def information(self, file):
        try:
            with open(file + '.txt', 'r') as filed:
                user_list = filed.readlines()
                for user in user_list:
                    with open(user + '.txt', 'w') as file_cool:
                        skill = input(f"What is " + user + "good at? ")
                        file_cool.write(user + "is good at " + skill)
        except FileNotFoundError as error:
             return error
        finally:
             return "Finished methoding program"
