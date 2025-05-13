names=["Alma", "Blerta", "Dhurata", "Shpati"]
for name in names:
    print(name)

# Shembulli 2
sentence_shembulli="5Hello, World5"
for char in sentence_shembulli:
    if char.isalpha(): #Kthen true ose false if char is letter
        print(char)

# Shembulli  3 me range function
for numri in range(1,6): #range(x,y) x-ku fillon y-ku mbaron mirepo nuk perfshihet y
    print(numri)

# Find Max ne nje list
numrat=[3,45,55,45,23,12,94,100,0,101]
max=numrat[0]
for num in numrat:
    if num>max:
        max=num
print("The max value of the list is: ",max)