class Car:
    def __init__(self,name,model):
     self.name = name             #instance variable
     self.model_year = model       #instance variable
     self.wheel = 4                  #instance variable
    def view(self):                 #instance method 
       print("Model year of this", self.name, "is",  self.model_year )
       print("It is a", self.wheel, "wheel car")

#-------------------------------------------------------------------
       
c1 = Car("BMW", 2016)
c1.view()
c1.name = "Rickshow"
c1.wheel = 3
c1.view()
print("_______________________________")

c2 = Car("Audi", 2018)
c3 = Car("Toyota", 2004)
c4 = Car("Mini", 1999)
c5 = Car("Lexus", 1966)
c2.view()
c3.view()
c4.view()
c5.view()