class Student:
    uni_name = "DIU"
    
    def  __init__(self, name, id):
        self.name = name
        self.id = id
        
    def details (self):
       print("Name: ", self.name, "Id: ", self.id, Student.uni_name)
    
    @classmethod
    def up_uni_name(cls, u_mame):
        cls.uni_name = u_mame
        
#==============================================================================

s1 = Student("Bob", 11)
s2 = Student("Carol", 22)
s1.details()
s2.details()
Student.up_uni_name("Brac University")
s1.details()
s2.details()
print(s1.__dict__)