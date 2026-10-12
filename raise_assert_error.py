
# try:
#     number = int(input("Enter a number : "))
#     if number < 0:
#         raise ValueError("negative")
# except ValueError as i:
#     if str(i) == "negative":
#         print("negative number is not allowed")
#     else:
#         print("enter valid number")
        
# else:
#     print("you enterted number :",number)



# class Student:
#     def __init__(self,age):
#         assert age >= 18 , "Age must be 18 or above"
#         self.age = age
# try:
#     student = Student(14)
# except AssertionError as e:
#     print("Assertion error :",e)



# class InsufficientError(Exception):
#     pass

# class Bankaccount:
    
#     def __init__(self,balance=0):
#         assert balance > 0 , "negative value are not allowed"
#         self.balance = balance
        
        
#     def withdraw(self,amount):
#         assert amount > 0 , "negative value are not allowed"
#         self.amount = amount
            
#         if amount > self.balance:
#             raise InsufficientError(f"you can not withdraw because balance is {self.balance} or withdraw amount is {amount}")
        
#         self.balance -= amount
#         print("withdraw successful !")
#         print(f"your current balance is {self.balance}")


#     def deposit(self,amount):
#         assert amount > 0 , "negative value are not allowed"
#         self.amount = amount
        
#         self.balance += amount
#         print("Deposit successful !")
#         print(f"your current balance is {self.balance}")
        
# try:
#     balance = float(input("Enter your balance: "))
#     account = Bankaccount(balance)

#     withdraw_amount = float(input("Enter withdrawal amount: "))
#     account.withdraw(withdraw_amount)

#     deposit_amount = float(input("Enter deposit amount: "))
#     account.deposit(deposit_amount)
    

# except ValueError:
#     print("Invalid input! Please enter numbers only.")
# except AssertionError as e :
#     print("AssertionError : ",e)
# except InsufficientError as e:
#     print("InsufficientError : ",e)


# ----------- lab work questions

# **

# try :
#     number = int(input("Enter a number : "))
#     if number < 0:
#         raise ValueError("negative number is not allowed")
# except ValueError as e:
#     print(f"Error : {e}")
# else:
#     print(f"you entered number : {number}")
    
    
# **

# def check_enven(number):
#     if isinstance(number,int):
#         if number % 2 != 0:
#             raise ValueError("enter even number only")
#         else:
#             print("number : ",number)
#     else:
#         raise TypeError("input must be an integer")
        
# try:
#     value = check_enven(79)
# except TypeError as e:
#     print(f"TypeError : {e}")
# except ValueError as e:
#     print(f"ValueError : {e}")


# **

# try:
#     age = int(input("Enter your age : "))
#     assert age > 18 , "Age must me 18 or above !"
# except AssertionError as e:
#     print("AssertionError : ",e)


# **

# while True :
#     def check_palindrome(str_value):
#         assert str_value.strip() != "" , "value cannot be empty !!" 

#         if str_value == str_value[::-1]:
#             print("It's palindrome !")
#         else:
#             print("It's not palindrome !")
#     try:
#         check_palindrome(input("Enter a value : "))
#     except AssertionError as e:
#         print(e)


# **

# class InsufficientBalanceError(Exception):
#     pass

# class Bankaccount:
    
#     def __init__(self,balance=0):
#         assert balance > 0 , "negative value are not allowed"
#         self.balance = balance
        
        
#     def withdraw(self,amount):
#         assert amount > 0 , "negative value are not allowed"
#         self.amount = amount
            
#         if amount > self.balance:
#             raise InsufficientBalanceError(f"you can not withdraw because balance is {self.balance} or withdraw amount is {amount}")
        
#         self.balance -= amount
#         print("withdraw successful !")
#         print(f"your current balance is {self.balance}")

# try:
#     balance = float(input("Enter your balance: "))
#     account = Bankaccount(balance)

#     withdraw_amount = float(input("Enter withdrawal amount: "))
#     account.withdraw(withdraw_amount)

# except ValueError:
#     print("Invalid input! Please enter numbers only.")
# except AssertionError as e :
#     print("AssertionError : ",e)
# except InsufficientBalanceError as e:
#     print("InsufficientError : ",e)


# **

# class InvalidEmailError(Exception):
#     pass

# def validate_email(email):
#     special_char = "@"
#     end_value = email.endswith((".com",".org"))
#     assert email.strip() != "" , "email cannot be empty !"
#     if special_char in email and end_value:
#         print("email is correct !")
#         print(f"your email is : {email}")
#     else:
#         raise InvalidEmailError("Invalid email enterted !")
    
# try:
#     validate_email(input("Enter your email : "))
# except AssertionError as e:
#     print(f"AssertionError : {e}")
# except InvalidEmailError as e:
#     print(f"InvalidEmailError : {e}")


# **

# class InvalidGradeError(Exception):
#     pass

# def marks_validate(marks):
#     assert marks.strip() != "" , "marks can not be empty !!"
    
#     marks = int(marks)
    
#     if marks < 0 or marks > 100:
#         raise ValueError("marks is not between 0 and 100 !")
#     else:
#         if marks >= 90:
#             print("your grade is : A")
#         elif marks >= 80:
#             print("your grade is : B")
#         elif marks >= 70:
#             print("your grade is : C")
#         elif marks >= 60:
#             print("your grade is : D")
#         elif marks >= 50:
#             print("your grade is : E")
#         elif marks >= 40:
#             print("your grade is : F")
#         else:
#             raise InvalidGradeError("you are FAIL in exam !")
        
# try:
#     marks_validate(input("Enter your marks : "))
# except AssertionError as e:
#     print(f"AssertionError : {e}")
# except ValueError as e:
#     print(f"ValueError : {e}")
# except InvalidGradeError as e:
#     print(f"InvalidGradeError : {e}")
            
        


