from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    def eat(self):
        print("I am eating")
        
#===========================================================

class Dog(Animal):
    def make_sound(self):
        print("Dog is Barking")

#===========================================================
       
d1 = Dog()
d1.make_sound()
d1.eat()