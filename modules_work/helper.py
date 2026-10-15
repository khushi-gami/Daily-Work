import math
def result(marks):
    print(f"your got score marks {marks} in exam !!")
    
def factorial(number):
    print(f"factorial of the numeber {number} is : ",math.factorial(number))
    
if __name__ == "__main__":
    print("this script excuted directly !")
    result(90)
    factorial(5)
else:
    print("the script import as module !")