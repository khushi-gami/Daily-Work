class Payment():
    def pay(self):
        print("Payment is processing..")
    
class Cash(Payment):
    def pay(self,amount):
        print("Payment using cash..")
        print(f"payment amount : {amount}")
        print("Payment done by cash.")

class Card(Payment):
    def pay(self,amount):
        print("Payment using card..")
        print(f"payment amount : {amount}")
        print("Payment done by credit / debit card.")

class UPI(Payment):
    def pay(self,amount):
        print("payment threw UPI..")
        print(f"payment amount : {amount}")
        print("Payment done by UPI.")

Payments = [Cash(),Card(),UPI()]

for payment in Payments:
    payment.pay(10000)

    print("----------------------")

# message = Payment()
# message.pay()
# cash = Cash()
# cash.pay(20000)
# print("-------------------")
# credit = Card()
# credit.pay(30000)
# print("-------------------")
# upi = UPI()
# upi.pay(40000)



class Calculator:
    def add(self,a,b=0,c=0):
        return a + b + c

sum = Calculator()
print(sum.add(5))
print(sum.add(5,10))
print(sum.add(5,10,15))




class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
animals = [Dog(),Cat()]
for animal in animals:
    animal.sound()




class Employee:

    def display(self):
        print("employee details..")

class Manager(Employee):

    def __init__(self,name,department):
        self.name = name
        self.department = department
    def display(self):
        print(f"{self.name} ia a manager of {self.department} department..")

class Developer(Employee):

    def __init__(self,name,language):
        self.name = name 
        self.language = language
    def display(self):
        print(f"{self.name} is a developer , they working with {self.language} language..")

manager = Manager("Ramesh","IT")
developer = Developer("Radhika","Java")
employees = [manager,developer]
for employee in employees:
    employee.display()




class Payment:

    def pay(self,amount):
        print("Detials of payment..")

class UPI(Payment):

    def pay(self,amount):
        print(f"Paid ₹{amount} using UPI")

class CreditCard(Payment):

    def pay(self,amount):
        print(f"Paid ₹{amount} using Credit Card")

class Cash(Payment):

    def pay(self,amount):
        print(f"Paid ₹{amount} using Cash")
        
payments = [UPI(),CreditCard(),Cash()]
for payment in payments:
    payment.pay(1000)
    

    
# lab questions ----------------------

# **

def add(a,b):
     print(a + b)
add(10,50)
add("Amazing","Python")

# **

class Shape:
    def area(self):
        print("calculatig the area of circle and rectangle..")
class Rectangle(Shape):
    def area(self,width,height):
        print("Area of Rectangle : ",width * height)
class Circle(Shape):
    def area(self,radius):
        print("Area of Circle : ",3.14 * radius * radius)
shape = Shape()
circle = Circle()
rectangle = Rectangle()
shape.area()
circle.area(2)
rectangle.area(20,30)

# **

string1 = "khushi"
list1 = [10,20,30,40]
dictionary1 = {
    "name" : "khushi",
    "age" : 50,
    "learn" : "AI/ML"
}
print(len(string1))
print(len(list1))
print(len(dictionary1))

# **

class Transport:
    def travel(self):
        pass
class Train(Transport):
    def travel(self):
        print("Travel by train..")
class Plane(Transport):
    def travel(self):
        print("Travel by plane..")
transports = [Train(),Plane()]
for transport in transports:
    transport.travel()

# **

class Calculator:
    def multiply(self,*args):
        result = 1
        for i in args:
            result *= i 
        print(f"multiply :",result)
calculator = Calculator()
calculator.multiply(1,2,3,4)
calculator.multiply(5,4)

# **

class Animal:
    def speak(sdelf):
        print("animals makes sound..")
class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
animals = [Animal(),Dog(),Cat()]
for animal in animals:
    animal.speak()

# **

class Vehicle:
    def start(self):
        pass
    
class Bike(Vehicle):
    def start(self):
        print("Bike starts with with kick")
        
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
        
bike = Bike()
bike.start()
car = Car()
car.start()

# **

class Printer:
    def print(self,*args):
        for i in args:
            print(i)
printer = Printer()
printer.print("Hello")
printer.print(100)
printer.print("Age",20)

# **

class Person:
    def learn(self):
        pass
class Student(Person):
    def learn(self):
        pass
print(issubclass(Student,Person))

# **

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
        print(f"my name is {self.name}, i'm from {self.department} department , i got salary {self.salary}")
manager = Manager("khushi",100000,"IT")

# **

class Grandparent:
    def family(self):
        pass
class Parent(Grandparent):
    def family(self):
        pass
class Child(Parent):
    def family(self):
        pass
print(issubclass(Parent,Grandparent))
print(issubclass(Child,Parent))

# **

class Base:
    def display(self):
        print("This is Base class..")
class Derived(Base):
    def display(self):
        super().display()
        print("This is derived class..")
values = [Base(),Derived()]
for value in values:
    value.display()

# **

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Admin(User):
    def __init__(self,name,age,designation):
        super().__init__(name,age)
        self.designation = designation
        print(f"I'm {self.name}. I'm {self.age} years old , currently I'm working as {self.designation} in a company..")
admin = Admin("Tanvi",32,"Data Analyst")
    

        






    