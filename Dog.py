class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def update_color(self,color):
        self.color = color

    def update_name(self,name):
        self.name = name
    
    def poke(self):
        print(self.color, self.name, "is smiling")

#---------------------------------------------------------------
d1 = Dog("Rover", "Brown")
d2 = Dog("Cookiz", "White")
d1.poke()
d1.update_color("Red")
d1.update_name("Shuji")
d1.poke()

print("-----------------------------------------")

d2.poke()

print("-----------------------------------------")

print(d1.__dict__)
print(d2.__dict__)

print("-----------------------------------------")

print(dir(d1))
print(dir(d2))

