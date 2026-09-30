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




class Animal:
    def sound(sdelf):
        print("animals makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog makes sound")
class Cat(Animal):
    def sound(self):
        print("Cat makes sound")
animals = [Animal(),Dog(),Cat()]
for animal in animals:
    animal.sound()




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
    












    