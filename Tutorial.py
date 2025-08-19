# n1 = 15
# n2 = 55

# print(n1 + n2)
# print(n1.__add__(n2))

#================================================

# class data:
#     def __init__(self,x):
#         self.x = x
#     def __add__(self,other):
#         return self.x + other.x   
# #====================================

# num1 = 10
# num2 = 20
# str1 = "CSE"
# str2 = "334"
# print(num1+num2)
# print(str1+str2)

class House:

    def __init__(self,w,d):
        self.window = w     #instance variable
        self.door = d       #instance variable

    def view(self):
        print("Window:", self.window, "door:", self.door)
       
        
    def __add__(self,other):
        new_window = self.window + other.window
        new_door = self.door+ other.door
        return "New house has "+str(new_window)+" windows and "+str(new_door)+" doors."
        
#=====================================================================
h1 = House(6,2)
h2 = House(4,5)
h1.view()
h2.view()
print(h1 + h2)