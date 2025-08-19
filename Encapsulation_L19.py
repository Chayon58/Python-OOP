class student:
    def __init__(self,X,Y):
        self.X = X
        self. __Y = Y
        
    def details(self):
        print("X:", self.X, "Y:", self.__Y)
        self.__method()
        
    def __method(self):
        print("Private Method Executed")
        
#=============================================================

s1 = student("Nikita", 22)
s2 = student("Shupratim", 23)
# s1.__method()
s1.details()