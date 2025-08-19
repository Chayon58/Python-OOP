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
        
    @classmethod
    def from_string(cls,info):
        name, id = info.split("-")
        obj  = cls(name, id)
        return obj
    
#====================================================================
s1 =  Student("John", "A001")
s2=  Student.from_string("Johny-A002")
s1.details()
s2.details()