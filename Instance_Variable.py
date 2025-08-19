class Student:
    def __init__(self,name,id):    #Constructor
        self.name = name   #instance Variable
        self.id = id   #instance Variable
        #print("A student object Created")
        
    def details(self):
        print("Name: ",self.name, " ID: ",self.id) 

#========================================================

s1 = Student("Mamun", 21)  
s2 = Student("Sumon", 22)
s1.name = "Ayon"
s1.details()
print("--------------------")
s2.name = "Moumita"
s2.details()