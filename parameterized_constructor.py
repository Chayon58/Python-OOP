class Student:
    def __init__(self,name,id):
        self.name = name   #instance Variable
        self.id = id   #instance Variable
        #print("A student object Created")

#========================================================

s1 = Student("Shanchita", 21)
s2 = Student("Debadrita", 22)

s1.id = 23
print(s1.name)
print(s1.id)
print(s2.name)
print(s2.id)