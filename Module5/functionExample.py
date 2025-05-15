from email.policy import default

from pyexpat.errors import messages

total=0

for number in range(1,11):
    if number%2==0:
        total+=number
print("The sum of even numbers from 1 to 10 is ",total)

# This is defining a function keyword def- in pyrhon defines functions. greet-emri i funlsionit
def greet():
    print("Hello World")

# this is how we use the function
greet()

def greet_person(name):
    print("Hello", name)

greet_person("Alma")

# This type of function returnes something in this case a num
def shuma(x,y):
    z=x+y
    return z
rezultati=shuma(3,4)
print("3+4= ", rezultati)

# local variables- variablat e deklaruara perbrenda nje funksioni
def greet(name):
    messages=f"hello,{name}!"
    print(messages)
greet("Alma")
# print(messages) - this outputs an error bc the message variable is defined only for the function

# argumentet dhe definimi i tyre
def greet_person(name,greeting="Hello"):
    message=f"{greeting}, {name}"
    return message
default_greeting=greet_person("Alma")
print(default_greeting)
custom_greeting=greet_person("Alma","Hi")
print(custom_greeting)

pershendetje="Hi"
def greet_people(name):
    global pershendetje
    return f"{pershendetje}, {name}"
variabla=greet_people("Alma")
print(variabla)