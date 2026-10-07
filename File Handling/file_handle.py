

# write mode(w)

# languages = ["java\n","python\n","javascript\n","c++\n","r\n","go\n"]
# demo_file = open('demo.txt','w')
# demo_file.write("This a demo file..")
# demo_file.write("Here you can add all the text , whatever you want..")
# demo_file.writelines(languages)

# demo_file.close()
# print("demo file is created with some information..")


# read mode(r)

# read_file1 = open('demo.txt','r')
# file_content1 = read_file1.read()
# print(file_content1)

# read_file1.close()


# readline mode(r)

# read_file2 = open('read.txt','r')
# file_content2 = read_file2.readline()

# while file_content2:
#     print(file_content2.strip())
#     file_content2 = read_file2.readline()

# read_file2.close()


# # readlines mode(r)

# read_file3 = open('read.txt','r')
# file_content3 = read_file3.readlines()
# # print(file_content3)
# print()
# for line in file_content3:
#     print(line)

# read_file3.close()


# don't need to close file with "with" keyword..
# with open('read.py') as file:
#     data = file.read()
# print(data)


# append mode()

# file = open("sample.txt","a")
# file.write("I am learn AI/ML.")

# file.close()


# read + write mode (r+)

# file = open("File Handling/demo.txt","r+")
# print(file.read())
# # file.seek(0)
# file.tell()
# file.write("Vivek sir is conducting our lectures..")

# file.close()


# write + read mode(w+)

# file = open("File Handling/sample.txt","w+")
# file.write("I'm very happy today..huu huu..")

# file.seek(0)
# print(file.read())

# file.close()


# append + read mode (a+)

# file = open("File Handling/sample.txt","a+")
# file.write("This content is added..")
# file.seek(0)
# print(file.read())

# file.close()


# write binary mode (wb)

# file = open("File Handling/sample.bin","wb") 
# content = b"Bin file was created..!!"
# file.write(content)

# file.close()


# read binary mode(rb)

# file = open("File Handling/sample.bin","rb")
# print(file.read())

# file.close()


# # append binary mode(ab)

# file = open("File Handling/sample.bin","ab")
# content = b"I append this content in bin file.."
# file.write(content)

# file.close()


# read + write binary mode (r+b)

# file = open("File Handling/sample.bin","r+b")
# print(file.read())
# new_content  = b"I write this using r+b mode.."
# file.write(new_content)

# file.close()


# write + read mode (w+b)

# file = open("File Handling/sample.bin","w+b")
# new_content  = b"I write this using w+b mode.."
# file.write(new_content)
# file.seek(0)
# print(file.read())

# file.close()


# append + binary (a+b)

# file = open("File Handling/sample.bin","a+b")
# new_content  = b"I write this using a+b mode.."
# file.write(new_content)
# file.seek(0)
# print(file.read())

# file.close()

# print(file.name)
# print(file.mode)
# print(file.closed)





