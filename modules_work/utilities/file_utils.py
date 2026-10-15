
def writefile(fileame,text):
    with open(fileame,"w") as file:
        file.write(text)
        print("file written successfully.") 
        
        
def readfile(filename):
    with open(filename,"r") as file:
        return file.read()