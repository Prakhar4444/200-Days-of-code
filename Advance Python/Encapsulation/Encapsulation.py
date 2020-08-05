# Private variabkes can be accesed within the method
# Use double underscore" __ "  before variable name for Private variables

# Example of Private Variables

class myclass :
    __a = 10

    def display(self):
# using self beacuse of class , as it will refer to the particular class
        print(self.__a)

obj = myclass()

obj.display()

# We can not use
# print( myclass.__a)
# because it is a private variable and can not be accesed outside the class

# Example of Private Methods

class myclass2 :

    def __display1(self):
        print("This is calling of First Function")
    def display2(self):
        print("This is calling of Second Function")
        self.__display1()

obj2 = myclass2()
# obj.__display() Cannot do this because can not acces a private method outside the class

obj2.display2()
#can do this because display2 function will call display1 function Internally in th class


# Example of Encapsulation

class myclass3 :
    __empid  = 101
    def func(self,id):
        self.__empid = id
    def display4(self):
        print(self.__empid)

ob = myclass3()

ob.func(105)
ob.display4()