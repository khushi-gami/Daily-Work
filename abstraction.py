from abc import ABC , abstractmethod
import math

class Hotel_Booking(ABC):
    def __init__(self,name,days):
        self.name = name
        self.days = days
        
    def calculate_bill(self):
        pass
    
    def customer_name(self):
        print(f"Customer Name : {self.name}")
        
class Normal_Hotel(Hotel_Booking):
    def __init__(self,name,days,room_cost):
        super().__init__(name,days)
        self.room_cost = room_cost
        
    def calculate_bill(self):
        return self.days * self.room_cost
    
class Luxury_Hotel(Hotel_Booking):
    def __init__(self,name,days,room_cost,food_cost):
        super().__init__(name,days)
        self.room_cost = room_cost
        self.food_cost = food_cost
        
    def calculate_bill(self):
        return self.days * (self.room_cost + self.food_cost)
    
class Extra_luxury_Hotel(Hotel_Booking):
    def __init__(self,name,days,room_cost,food_cost,wifi_cost):
        super().__init__(name,days)
        self.room_cost = room_cost
        self.food_cost = food_cost
        self.wifi_cost = wifi_cost
        
    def calculate_bill(self):
        return days * (self.room_cost + self.food_cost + self.wifi_cost)
    

print("----------------------------------------------------------------------------")
print("Hotel Booking System :")        
print("----------------------------------------------------------------------------")
print("1. Normal Hotel ")
print("2. Luxury Hotel ")
print("3. Extra Luxury Hotel ")

choice = int(input("Enter your choice : "))
name = input("Enter your name : ")
days = int(input("Enter no. of days , you want to stay : "))
room_cost = 20000
food_cost = 3000
wifi_cost = 5000

if choice == 1 :
    message = "Normal Hotel : "
    customer = Normal_Hotel(name,days,room_cost)
    
elif choice == 2:
    message = "Luxury Hotel : "
    customer = Luxury_Hotel(name,days,room_cost,food_cost)
    
elif choice == 3:
    
    message = "Extra Luxuruy Hotel : "
    customer = Extra_luxury_Hotel(name,days,room_cost,food_cost,wifi_cost)
    
else:
    print("Invalid Choice..!")
    exit()
    
print("--------------------")
print("Hotel Booking Cost :")
print("--------------------")
print(f"For {message}")
customer.customer_name()
print("Customer Charge : ",customer.calculate_bill())


# **

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width

# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius * self.radius

# # shape = Shape()  --- this will raise error

# r = Rectangle(10, 5)
# print("Rectangle Area:", r.area())

# c = Circle(7)
# print("Circle Area:", c.area())



# # **

# class MLModel(ABC):

#     @abstractmethod
#     def train(self):
#         pass

#     @abstractmethod
#     def predict(self):
#         pass

# class LinearRegressionModel(MLModel):

#     def train(self):
#         print("Train Linear Regression Model..")
#     def predict(self):
#         print("Predictions (use Linear Regression Model)")

# class DecisionTreeModel(MLModel):

#     def train(self):
#         print("Train Decision Tree Model...")
#     def predict(self):
#         print("predictions (use Decision Tree Model)")

# linear = LinearRegressionModel()
# decision_tree = DecisionTreeModel()

# print("Linear Regression Model:")

# linear.train()
# linear.predict()

# print()

# print("Decision Tree Model:")

# decision_tree.train()
# decision_tree.predict()     

                                                                                                                                                              


