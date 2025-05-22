#Error handling Try,  Except, Finally
#Try - writting of the needed code
#Except - what happens if an error happens in the try part
#Finally - Part of code that is always run

#This is dedicated for errors that programmers do not predict

#first example
# try:
#     print("Pjesto dy numra")
#     nr1=int(input("Shkruani nr1:"))
#     nr2=int(input("Shkruani nr2:"))
#     resultati=nr1/nr2
#     print("Rezultati:",resultati)
# except ZeroDivisionError:
#     print("Ke gabu per shkak qe je duke pjestuar me 0")

#second example
fruits={
    "Apples":5,
    "Banana":6,
    "Orange":7
}
try:
    print(fruits["Banana"])
except KeyError:
    print("The key does not exist in the dictionary")



text="This is not a number"
#third example
try:
    text_to_int=int(text)
except Exception as e:
    print("An error occorred while parsing the data:", e)

#forth example
try:
    resultati=10/0
except ZeroDivisionError:
    print("Division by zero error occorred")
else:
    print("Division successful, Result:",resultati)


#fifth example
try:
    resultati=10/5
except ZeroDivisionError:
    print("Division by zero error occorred")
finally:
    print("This part of code always runs")