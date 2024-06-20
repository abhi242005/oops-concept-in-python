# It is process of combing variables and methods
# Encapsulation by class
class Car:
    def newcar(self,name):
        print(f"my newcar is {name}")
class color:
    c='black'
    num='143'
    def details(self):
        print(f"car color is {self.c} and number is {self.num}")
s=Car()
s.newcar('benz')
s1=color()
s1.details()