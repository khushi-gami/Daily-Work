# 1.

# file = open("File Handling_Lab/sample.txt","w")
# file.write("Python is a versatile programming language.")
# file.close()


# 2.

# file = open("File Handling_Lab/sample.txt","r")
# content = file.read()
# print(content)
# file.close()

# file = open("File Handling_Lab/sample.txt","w")
# file.write("Learning file handling in Python is fun!")
# file.close()


# 3.

# file = open("File Handling_Lab/sample.txt","r")
# content = file.readlines()
# for line in content:
#     print(line)
# file.close()


# 4.

# file = open("File Handling_Lab/notes.txt","w")
# file.writelines("Python is easy to learn. \n It has numerous libraries. \n File handling is one of its features.\n")
# file.close()


# 5.

# file = open("File Handling_Lab/notes.txt","a")
# file.write("Python supports multiple modes of file handling.")
# file.close()


# 6.

# file = open("File Handling_Lab/notes.txt","rb")
# content = file.read()
# print(content)
# file.close()


# 7.

# file = open("File Handling_Lab/notes.txt","r")
# content = file.read()
# words = len(content.split())
# characters = len(content)
# lines = len(content.splitlines())
# print(f"words : {words}")
# print(f"characters : {characters}")
# print(f"lines : {lines}")
# print(content)
# file.close()


# 8.

# file = open("File Handling_Lab/notes.txt","r+")
# content = file.read()
# print(content)
# file.seek(0, 2)
# file.write("This file was last modified by adding this sentence.")
# file.close()


# 9.

# file = open("File Handling_Lab/notes.txt","r")
# content = file.read()
# lines = content.splitlines()
# value = input("Enter a word , you want to find : ")
# for line_number, line in enumerate(lines, start=1):
#     if value in line:
#         print(f"{value} found at line {line_number}")


# 10.
  
# source_file = open("File Handling_Lab/source.txt","r")
# content = source_file.read()
# print(content)

# backup_file = open("File Handling_Lab/backup.txt","w")
# backup_file.write(content)

# source_file.close()
# backup_file.close()


# 11.

# write mode(w)

# file = open("File Handling_Lab/demo.txt","w")
# file.write("This is demo file..")
# file.write("Here we have demo content..")
# file.close()

# write mode(r)

# file = open("File Handling_Lab/demo.txt","r")
# demo_content = file.read()
# print(demo_content)
# file.close()

# append mode(r)

# file = open("File Handling_Lab/demo.txt","a")
# file.write("THhis is append line I add into the demo file..")
# file.close()

# read + write mode (r+)

# file = open("File Handling_Lab/demo.txt","r+")
# demo_content = file.read()
# print(demo_content)
# file.write("\n I add this line using r+ mode !")
# file.close()

# write + read mode (w+)

# file = open("File Handling_Lab/demo.txt","w+")
# file.write("I add this line using w+ mode !")
# file.seek(0)
# demo_content = file.read()
# print(demo_content)
# file.close()

# append + read mode (a+)

# file = open("File Handling_Lab/demo.txt","a+")
# file.write("I add this line using a+ mode !")
# file.seek(0)
# demo_content = file.read()
# print(demo_content)
# file.close()










