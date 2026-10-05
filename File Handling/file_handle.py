# write mode(w)

languages = ["java\n","python\n","javascript\n","c++\n","r\n","go\n"]
demo_file = open('demo.txt','w')
demo_file.write("This a demo file..")
demo_file.write("Here you can add all the text , whatever you want..")
demo_file.writelines(languages)

demo_file.close()
print("demo file is created with some information..")


# read mode(r)

read_file1 = open('demo.txt','r')
file_content1 = read_file1.read()
print(file_content1)

read_file1.close()


# readline mode(r)

read_file2 = open('read.txt','r')
file_content2 = read_file2.readline()

while file_content2:
    print(file_content2.strip())
    file_content2 = read_file2.readline()

read_file2.close()


# readlines mode(r)

read_file3 = open('read.txt','r')
file_content3 = read_file3.readlines()
# print(file_content3)
print()
for line in file_content3:
    print(line)
read_file3.close()


# don't need to close file with "with" keyword..
with open('read.py') as file:
    data = file.read()
print(data)


