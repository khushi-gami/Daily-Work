import math
import random
import uuid
import time

# lab questions

# **

# print("square root : ",int(math.sqrt(25)))
# print("factorial : ",math.factorial(5))
# print("power : ",int(math.pow(2,3)))

# **

# def circle_area():
    
#     radius = 7
#     area = math.pi * math.pow(radius,2)
#     print("area of circle : ",area)
#     print("natural logarithm of a number : " , math.log(10))
    
# circle_area()

# **

# def trigonometric():
    
#     angle = 30
#     radian = math.radians(angle)
#     print("sin radian : ",math.sin(radian))
#     print("cos radian : ",math.cos(radian))
#     print("tan radian : ",math.tan(radian))
    
# trigonometric()

# **

# def calculate_value():
    
#     value = 4.6
#     print("ceil : ",math.ceil(value))
#     print("floor : ",math.floor(value))
#     print("absolute :",math.fabs(value))    
    
# calculate_value()

# **

# def random_numebr():
#     number_list = []
#     for i in range(1,11):
#         i = random.randint(1,100)
#         number_list.append(i)
#     print("random number list : ",number_list)
# random_numebr()

# **

# def dice():

#     number = random.randint(1,6)
#     print("dice : ",number)
    
#     list_numbers = [1,2,3,4,5,6]
#     random.shuffle(list_numbers)
#     print("suffle : ",list_numbers)
    
# dice()

# **

# def choice():
#     list_values = ["python","java","c","c++","javascipt","r","go"]
#     print("random list value : ",random.choice(list_values))
# choice()

# **


# def game():
#     game_values = ["rock", "paper", "scissors"]

#     user_value = input("Enter rock/paper/scissors: ").lower()

#     if user_value not in game_values:
#         print("Invalid choice!")
#         return

#     random_value = random.choice(game_values)

#     time.sleep(1)
#     print("Your choice:", user_value)
#     print("Computer choice:", random_value)

#     time.sleep(1)

#     if user_value == random_value:
#         print("Draw!")

#     elif (
#         (user_value == "rock" and random_value == "scissors")
#         or (user_value == "paper" and random_value == "rock")
#         or (user_value == "scissors" and random_value == "paper")
#     ):
#         print("You win!")

#     else:
#         print("Computer wins!")

# game()

