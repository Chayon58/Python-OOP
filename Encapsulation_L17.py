class student:
    def __init__(self,name,id):
        self.name = name
        self. __id = id
    def details(self):
        print("Name:", self.name, "id:", self.__id)
    def updt_ID(self,id):
        if(id>0):
            self.__id = id
        else:
            print("Invalid ID")
            
#===========================================================

s1 = student("MP", 22)
s2 = student("DP", 23)

s1.updt_ID(33)
print(s1.__dict__)

s1.details()
s2.details()
