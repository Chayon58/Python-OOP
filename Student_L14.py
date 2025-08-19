class Student:

    def __init__(self, *info):
        if len(info) == 3:
         self.name = info[0]
         self.id = info[1]
         self.cgpa = [2]
        if len(info) == 2:
         self.name = info[0]
         self.id = info[1]
        if len(info) == 1:
         self.name = info[0]

        print("A student id created")
#======================================================================
         
s1 = Student("Carrol", 33, 3.46)
s1 = Student("Bob", 33)
s1 = Student("Mike")
s1 = Student()

