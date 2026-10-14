from functools import reduce

# lab questions

# **

# numbers = [4,7,9,2,5,4,1]

# ascending_order = sorted(numbers)
# descending_order = sorted(numbers,reverse=True)

# print("ascending : ",ascending_order)
# print("descending : ",descending_order)


# **

# words = ["apple","banana","kiwi","mango","fig"]

# len_words = sorted(words,key=len)
# last_letter = sorted(words,key = lambda x : x[-1])

# print("sorted by length : ",len_words)
# print("sorted by last letter : ",last_letter)


# **

# student_list = [
#     {"name" : "khushi","age":25},
#     {"name" : "priya","age":30},
#     {"name" : "maya","age":10},
#     {"name" : "tara","age":50},
#     {"name" : "shivani","age":87},
# ]
# sort_by_age = sorted(student_list,key = lambda student : student["age"])
# print("Sort by age : ",sort_by_age) 


# **

# words = ["apple","banana","kiwi","mango","fig"]

# uppercase = list(map(lambda x : x.upper(),words))
# print("uppercase : ",uppercase)


# **

# numbers = [4,7,9,2,5,4,1]
# square = list(map(lambda number : number * number,numbers))
# math_square = list(map(pow , numbers , [2] * len(numbers)))
# print("square : ",square)
# print("square : ",math_square)


# **

# price = [100,123,142,356]

# add_tax = list(map(lambda x : int(x + (x * 18 / 100)),price))
# print("add tax value : ",add_tax)


# **

# numbers = [4,7,9,2,5,4,1]
# even_numbers = list(filter(lambda x : x % 2 == 0,numbers))
# print("even numbers : ",even_numbers)


# **

# words = ["apple","banana","kiwi","mango","fig"]

# updated_words = list(filter(lambda x : len(x) > 5,words))
# print("len greater than 5 : ",updated_words)


# **

# student_score = [45,52,20,39,35,78,95]

# updated_score = list(filter(lambda x : x >= 40,student_score))
# print("student score above 40 : ",updated_score) 


# **

# numbers = [4,7,9,2,5,4,1]

# product = reduce(lambda x , y : x * y,numbers)
# print("product of all the numbers : ",product)


# **

# words = ["apple","banana","kiwi","mango","fig"]

# higest_len = reduce(lambda x , y : x if len(x) > len(y) else y ,words)

# print("longest word : ",higest_len)


# **

# words = ["Python", "is", "easy", "to", "learn"]

# sentence = reduce(lambda x , y : x + " " + y,words)

# print("Sentence : ",sentence)


