class House:

    def __init__(self):
        self.window = 4     #instance variable
        self.door = 2       #instance variable

    def view(self):
        print("Window:", self.window, "door:", self.door)

#--------------------------------------------------------------

h1= House()
h1.window = 6
h2= House()
h2.door = 3
h1.view()
h2.view()
