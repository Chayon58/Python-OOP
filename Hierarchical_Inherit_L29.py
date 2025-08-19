class Student:  #parent class
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def details(self):
        print("Name: ", self.name, "ID: ", self.id)
#===============================================================
class CSEStudent(Student): #CSE is the department of Computer Science and Engineering
    def __init__(self, name, id, labs):
        super().__init__(name,id)
        self.no_of_labs = labs
    def cry(self):
        print("CSE student crying because of", self.no_of_labs, "labs")
#=======================================================================
class BBAStudent(Student):
    
    def party(self):
        print("All day party")   
#=======================================================================
s1 = CSEStudent("Bob", 11, 3)
s2 = BBAStudent("Carol", 33)
s1.details()
s2.details()
s1.cry()
s2.party()
     
    