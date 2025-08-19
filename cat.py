class Cat:

    def __init__(self,color,action):
        self.color = color
        self.action = action

    def view(self):
        print( self.color, "cat is", self.action)

    def compare(self, ct):
        if self.action == ct.action:
            print("Both cats are ", self.action)
        else:
            print("They are different")


#====================================================================
c1 = Cat("white","Jumping")       
c2 = Cat("Black","Singing")   
c1.view()
c2.view()    

print("========================================")

c1.compare(c1)
c2.compare(c1)