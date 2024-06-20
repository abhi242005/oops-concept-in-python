#constructor
#class Vehicle:
#    def __init__(self,name,number):
#       self.number=number
 #   def display(self):
  #      print(self,name,self.number)
#car=Vehicle("Alto",1234)
#car.display()
#car1=Vehicle("Glanza",1430)
#car1.display()
#destructor
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def  __del__(self):
        print("destructor has been executed")
    def display(self):
        print(self.name,self.age)
p=Person("abhinaya",18)
del p
p.display()'''
# single inheritance
'''class book:#parent
    def authorname(self):
        print("this book is author function")
class bookname(book):#child
    def book(self):
        print("the book name is secret")
c=bookname()
c.authorname()
c.book()'''
#multiple inheritance
'''class book:#parent
    def authorname1(self):#parent
        print("this book is author function")
class bookname:#child
    def authorname2(self):#parent
        print("the book is 2nd book ")
class bookname1(book,bookname):
    def bookname1(self):#child
        print("the book name is secret")
c=bookname1()
c.bookname1()
c.authorname2()
c.authorname1()'''
#multi level inheritance
'''class book:
    def authorname(self):
        print("this book is author function")
class book1(book):
    def authorname1(self):
        print("the book is 2nd book")
class book2(book1):
    def authorname2(self):
        print("the book name is secret")
c=book2()
c.authorname()
c.authorname2()
c.authorname1()'''
# hierarical inheritance
'''class book:#parent
    def authorname(self):
        print("this book is author function")
class book1(book):#child
    def authorname1(self):
        print("the book is 2nd book")
class book2(book):#child
    def authorname2(self):
        print("the book name is secret")
c=book2()
c.authorname2()
c.authorname()
c1=book1()
c1.authorname1()
c.authorname()'''
#hirarcial and multiple hybrid
'''class book:
    def bookname(self):
        print("this book is author function")
class book1(book):
    def bookname1(self):
        print("the book is 2nd book")
class book2(book):
    def bookname2(self):
        print("the book name is secret")
class book3:
    def bookname3(self):
        print("xyz")
class book4(book,book3):
    def bookname4(self):
        print("Abhinaya")
c=book1()
c.bookname1()
c.bookname()
c1=book2()
c1.bookname2()
c1.bookname()
c2=book4()
c.bookname()
c1.bookname2()
c2.bookname3()
c2.bookname4()'''
# solution for diamond problem in multiple inheritance in python
class A:
    name='CSE'
    def branch(self):
        print(f"my branch is",self.name)
class B:
    def branch(self,name1):
        print(f"my branch name is {name1}")
class C(B,A):# First inherited class is B, so the priority order is B->A
    def child(self,college):
        print(f" the college name is {college}")
'''class C(A,B):# First inherited class is A, so the priority order is A->B
    def child(self,college):
        print(f" the college name is {college}")'''
x=C()
x.branch('ECE')
#x.branch()
x.child('IARE')





'''class A:
    def method_a(self):
        print("In method a")
    def common_method(self):
        print("I'm in class A")
class B:
    def method_b(self):
        print("In method b")
    def common_method(self):
        print("I'm in class B")
class C(A,B):  # First inherited class is A, so the priority order is A->B
    pass
ob = C()
ob.method_a()
ob.common_method()'''

    


    
