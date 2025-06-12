lines=["Hello World\n", "Welcome to Python\n"]
with open("example.txt","w") as file: #we open the file with premmisions to write
    file.writelines(lines) #we write on multipule lines