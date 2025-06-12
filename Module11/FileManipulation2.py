import os
if os.path.exists("example.txt"):
    print("File Exists!!!")

name="Alice"
age = 30

with open("output.txt", "w") as file:
    file.write("Name: "+name+"\n")
    file.write("Age: "+str(age)+"\n")