# A method acting or producing different outputs in different circumstances.

# Types - Compile time & Runtime Polymorphism
# 1) Method overloading- same class & method name and different method signature
# 2) Method overriding - different class, same method name & method signature

# Method overriding - It takes the latest method argument
class Family1:
    def parents(self,children,school):
        print(f"no.of children are {children} and their school name is {school}") 
    def parents(self,x,y):
        print(f,"the name of x is {x} and the name of y is {y}")
    def parents(self,a1,a2):
        print(f"the ages of children are {a1},{a2}")
class Family2:
    def parents(self,name):
        print(f"the child name is {name}")
ob=Family1()
ob.parents(2,'Kakatiya') #python takes latest positional argumentthe output:ages of children are 2,Kakatiya
ob.parents(18,16)#the ages of children are 18,16
ob=Family2()
ob.parents('Abhi')#the child name is Abhi
