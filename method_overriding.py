class A:
    def __init__(self):
        print("__init of class A")
    def method1(self):
        print("Olpo study")
    def method2(self):
        print("You will get all of my proparties and Methods")
#==================================================================
class B(A):
    def __init__(self):
        pass        #init faka rakha jabe na tai pass use korte hbe
    def method1(self):   #Method Overriding
        super().method1()  #parent er method call korte super use hoy
        print("Always Party")
#===================================================================
b1 = B()
b1.method1()
b1.method2()