class Parent():
    def __init__(self):
        self.name = "bob"
    def print_name(self):
        print (self.name)

class Child(Parent):
    def print_other(self):
        print ("joe")

child = Child()
child.print_name()