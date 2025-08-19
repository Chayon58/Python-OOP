class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
#===============================================================
class dummy:
    def __init__(self):
        self.val = 0
    def detail(self,std):
        print(std.name)
        print(std.id)
#=================================================
        
s1 = Student("Bob", 11)
d1 = dummy()

#d1.detail(s1.name)   #pass by value
#d1.detail(s1.id)


d1.detail(s1)

