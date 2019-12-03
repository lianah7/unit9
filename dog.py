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
        self.trick_list.append("roll over")
        print(self.name + " rolls over")

    def catch(self):
        self.trick_list.append("catch")
        print(self.name + " catches the ball")

    def bark(self):
        self.trick_list.append("bark")
        print(self.name + " barks at the mailman")

    def print_trick_list(self):
        if not self.trick_list:
            print(self.name + " has not performed any tricks yet.")
        else:
            print(self.name + " knows the following tricks:")
            for x in self.trick_list:
                print(x)

    



