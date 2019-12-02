class Dog:

    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        self.trick_list.append("sit")
        print(self.name + " sits")

    def lay_down(self):
        self.trick_list.append("lay down")
        print(self.name + " lays down")

    def roll_over(self):
        print(self.name + " rolls over")

    def cook(self):
        print(self.name + " cooks dinner")

    def bark(self):
        print(self.name + "barks at the mailman")

    def print_trick_list(self):



