class Animal:     #ParentClass
    def __init__(self,name):
         self.name = name
         
    def eat(self):
        print(self.name, "is eating")
        
#=======================================================

class Dog(Animal):     #ChildClass
    def bark(self):
        print(self.name, "is barking")
        
#========================================================

a1 = Animal("Linda")
d1 = Dog("Turbo")

# print(isinstance(a1,Dog))  #is a relationship amra "isinstance" function use koreo dekhte pari

print(issubclass(Dog, Animal))   #subclass relation check with "issubclass

# d1.bark()
# d1.eat()
# a1.eat()