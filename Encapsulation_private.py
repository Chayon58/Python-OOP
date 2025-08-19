class student:
    def __init__(self,name,id):
        self.name =name
        self.__id =id  #private variable
    
    def details(self):
        print("name:", self.name, "ID:", self.__id)
        
    
    def update_id(self,id):
        if(0>id):
            self.__id =id
            
        else:
            print("Invalid Id.Enter Id again")
    
#========================================================

s1 = student("Zhon", 11)
s2 = student("Abhi", 18)

s1.update_id(-666)

s1.details()
s2.details()