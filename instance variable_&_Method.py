class car:
    def __init__(self,name,model):
        self.name = name             #instance Variable
        self.model_year = model      #instance Variable
        self.wheel = 4               #instance Variable
        
    def view(self):                      #instance Method
        print("The Model Year of this", self.name, "is", self.model_year)
        print("It is a", self.wheel, "Wheel car")
        
#====================================================
c1 = car("BMW", 2016)
c2 = car("Audi", 2018)
c1.view()
c2.view()