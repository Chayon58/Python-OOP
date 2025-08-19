class House:
    def __init__(self):
        self.window = 4
        self.door = 2
    def view(self):
        print(self.window, "windows", self.door, "doors")
        
#========================================================
h1= House()
h2= House()
h1.window = 7
h2.door = 5
h1.view()
h2.view()
