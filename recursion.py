# print 5 to 1 --------------------------------------
def print_value(n):
    
    if n < 0:
        print("negative numebrs are not allowed !")
        return
    if n == 0:
        return

    print(n)
    print_value(n-1)
print_value(5)


# print 1 to 5 ---------------------------------------
def print_num(n):
    
    if n < 0:
        print("negative numbers are not allowed !")
        return 
    if n == 0:
        return

    print_num(n-1)
    print(n)
print_num(5)


# print sum of numebrs ---------------------------------
def sum_num(n):

    if n == 0:
        return 0

    return n + sum_num(n-1)
print("Sum : ",sum_num(5))


# print factorial of given number -----------------------
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)
print("Factorial : ",factorial(5))


# print even number -----------------------------

def even_num(n):

    if n == 0:
        return 
    
    even_num(n-1)
    if n % 2 == 0:
        print(n)

even_num(10)


# print odd number -----------------------------

def odd_num(n):

    if n == 0:
        return 
    
    odd_num(n-1)
    if n % 2 != 0:
        print(n)

odd_num(10)



# sum of all even number --------------------------

total = 0
def even_sum(n):
    global total
    if n == 0:
        return 

    even_sum(n-1)
    if n % 2 == 0:
        total += n
    return total 
print("Total of even numbers : ",even_sum(10))


# sum of all odd number --------------------------

total = 0
def odd_sum(n):
    global total
    if n == 0:
        return 

    odd_sum(n-1)
    if n % 2 != 0:
        total += n
    return total 
print("Total of even numbers : ",odd_sum(7))





































