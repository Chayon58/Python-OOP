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
        
    @staticmethod
    def check_department(id):
        if id[3:5] == '01': print ("CSE")
        elif id[3:5] == '41': print ("CS")
        
#=============================================================================
s1 =  Student("John", "11")
s2 =  Student("shaan", "47")
s1.details()
s2.details()
Student.check_department("14341007")