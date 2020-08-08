# In Python "ABC" is a predefined abstract class in Python.

# Abstract Class
from abc import ABC, abstractmethod

class A(ABC) :
    @abstractmethod
    def display(self):
        None

class b(A):
    def display(self):
        print("This is the Display method ")

obj = b()
obj.display()

# Example

class Animal(ABC) :
    @abstractmethod
    def eat(self):
        None
    @abstractmethod
    def age(self):
        None

class Tiger(Animal) :
    def eat(self):
        print("Tiger eats Non-Veg")

class Detail(Tiger) :
    def age(self):
        print("Max age is 50")

c = Detail()
c.age()
c.eat()

# Constructor in Abstract class
# Example

class Cal(ABC):
    def __init__(self,value):
        self.value1 = value

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class C(Cal) :
    def add(self):
        print(self.value1+100)
    def sub(self):
        print(self.value1-100)

d= C(500)
d.add()
d.sub()