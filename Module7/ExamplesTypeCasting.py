from reprlib import recursive_repr

from Module4.do_while import user_input

age=25
age_As_string=str(age)
print(age_As_string, " of type", type(age_As_string))

print(bool(0))#this is false bc 0 is false in booleaon
print(bool(42))#this is true bc 42 translates as 1(true in booleaon)

print(bool(""))
print(bool("Hello"))


# implicit typeCASTING
x=32
y=3.1
resultati=x+y
print(resultati, "of type ", type(resultati))

a=5
b="3"
resultati1=a*int(b)
print(resultati1,"of type",type(resultati))

c=4
resultati2="Hello"*c
print(resultati2, "type", type(resultati2))

# get 2 numbers from user input and sum them up
nr1=int(input("Num 1:"))
nr2=int(input("Num 2:"))
res=nr1+nr2
print(res)