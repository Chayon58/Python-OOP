class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def update_color(self,color):
        self.color = color
        
    def poke(self):
        print(self.color, self.name, "is smiling.")
        
#===================================================
d1 =Dog("Turbo", "white")
d2 =Dog("Linda", "Brown")
d1.poke()
d1.update_color("black")
d1.poke()
d2.poke()
