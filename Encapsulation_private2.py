class student:
    def __init__(self,name,id):
        self.name =name
        self.__id =id  #private variable
    
    def details(self):
        print("name:", self.name, "ID:", self.__id)
        
    
    def set_id(self,id):
        if(id>0):
            self.__id =id
            
        else:
            print("Invalid Id.Enter Id again")
        
    def get_id(self):
        return self.__id
    
    def set_name(self,name):
        self.name =name
    
    def get_name(self):   
        return self.name
    
    
#========================================================

s1 = student("Zhon", 11)
s2 = student("Abhi", 18)

s1.set_id(66)
print(s1.get_id())

s2.set_name("Dibbo")
print(s2.get_name())

s1.details()
s2.details()