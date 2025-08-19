class student:
    def __init__(self,name,id):
        self.name = name
        self. __id = id
        
    def details(self):
        print("Name:", self.name, "id:", self.__id)
        
    def set_ID(self,id):
        if(id>0):
            self.__id = id
        else:
            print("Invalid ID")
                    
    def get_id(self):
        return self.__id
    
    def set_name(self,name):
            self.name = name
                    
    def get_name(self):
        return self.name
            
#===========================================================

s1 = student("MP", 22)
s2 = student("DP", 23)

s1.set_ID(33)
s2.set_name("CP")

s1.details()
s2.details()
