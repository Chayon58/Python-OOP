from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def method1(self):
        pass

#================================================================
class B(A):
    @abstractmethod
    def method1(self):
     pass
        
#================================================================
class C(B):        
    def method1(self):
        print("Method1 is overridden")
        
    def method2(self):
        print("Method2 is overridden")

#=================================================================

c = C()
c . method1()
c . method2()
        
