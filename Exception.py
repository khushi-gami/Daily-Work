import math

# ---------------- Lab work questions

# **

# try:
#     num1 = float(input("Enter 1 number : "))
#     num2 = float(input("Enter 2 number : "))

#     result = num1 / num2
# except ValueError:
#     print("please enter valid number..")
        
# except ZeroDivisionError:
#     print("Cannot divided by zero..")

# else:
#     print("Result :" , result)


# **

# try:
#     numbers = [10,20,30,40,50]
#     result = numbers[7]
# except IndexError:
#     print("Index out of the range !")
# else:
#     print("result :",result)


# **
    
# file = None
# try:
#     filename = input("Enter filename : ")
#     file  = open(filename , "r")
#     content = file.read()

# except FileNotFoundError:
#     print("File not found.")
    
# else:
#     print("File content : ")
#     print(content)

# finally:
#     if file is not None:
#         file.close()
#     print("File Operation complete.")


# **

# try:
#     text = "Python"
#     result = text[7]
# except IndexError:
#     print("Index out of the range !")
# else:
#     print("result :",result)

# **

# try:
#     number = int(input("Enter a number: "))

#     if number < 0:
#         raise ValueError("negative")

# except ValueError as i:
#     if str(i) == "negative":
#         print("Number cannot be negative !")
#     else:
#         print("Please enter a valid integer !")

# else:
#     print(math.sqrt(number))
    
    








    
    
    

     
    

    
    
    





