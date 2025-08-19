class Student:    #class/design/blueprint
    
    def __init__(self, name, id):
     self.name = name      #instance variable
     self.id = id
     #print("A student object Created")

    def details(self):
        print("Name:", self.name, "ID:", self.id)

#variable = class_name()
s1 = Student("Mishkat",32)
s2 = Student("Diganta",33)
s1.id = 24
s1.details()
s2.details()

#print("s1",s1)
#print("s2",s2)
