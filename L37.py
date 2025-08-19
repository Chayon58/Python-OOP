from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def make_sound(self): 
        pass
    
    def eat(self):
        print("I am eating")
#=============================================
class Dog(Animal):
    def make_sound(self):
        print("Dog is Barkingg")
#=============================================
class cat(Animal):
    def make_sound(self):
        print("Meow Meow")
#=============================================
class Snake(Animal):
    def make_sound(self):
        print("Fushhh Fushhh")
#=============================================
d1 =Dog()
d1.eat()
d1.make_sound()
c1=cat()
c1.make_sound()
s1=Snake()
s1.make_sound()