class Student:  #Grandparent class
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def details(self):
        print("Name: ", self.name, "ID: ", self.id)
#===============================================================
class CSEStudent(Student): #parent class
    def __init__(self, name, id, labs):
        super().__init__(name,id)
        self.no_of_labs = labs
    def cry(self):
        print(self.name,"is crying because of", self.no_of_labs, "labs")
#===============================================================
class CSEFresher(CSEStudent):  #child class
    def enroll_CSE110(self):
        print(self.name,"Enrolled in CSE110")
#==========================================================
s1 = CSEStudent("Bob", 11, 3)
s2 = CSEFresher("Carol", 33,1)
s1.details()
s2.details()
s1.cry()
s2.cry()
s2.enroll_CSE110()