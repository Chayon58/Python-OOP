class Student:    #class/design/blueprint
    
    def __init__(self, name, id):
     self.name = name      #instance variable
     self.id = id
    def detail(self):
       print(self.name,self.id)

#variable = class_name()
s1 = Student("Mostakem",32)
s1.name= "Mostakem Obhe"
print(s1.name)
s1.detail()
#print(s1.name)
#s1.name= "Mishkat Roy"
#print(s1.name)

print("-----------------------------")

s2 = Student("Diganta",33)
s2.detail()
#print(s2.name)
#print(s2.id)
#s2.id = 24
#print(s2.id)


#print("s2",s2)
