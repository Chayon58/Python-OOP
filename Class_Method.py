class student:
    uni_name ="DIU"
    def __init__(self,name,id):
        self.name =name
        self.__id =id  #private variable
    
    def details(self):
        print("name:", self.name, "ID:", self.__id, student.uni_name)
        
    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name
        
#======================================================

s1 = student("Zhon", 11)
s2 = student("Abhi", 18)

s1.details()
s2.details()
student.up_uni_name("DIU University")
s1.details()
s2.details()