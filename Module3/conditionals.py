#kushtet kontrolloa e flow-it te programit
# == nese jane te barabarta dy variabla
#!= nese nuk jane te barabarta variablat
# < me e vogel se
# >me e madhe se
# <= dhe >=
# operatioret logjike
# and or not
from Module1.main import temperatura

#shembulli:
age=int(input("Sa vjeq jeni?"))
if age>=15:
    print("Accepted")
else:
    print("Code.org")

temperature=28
if temperature>30:
    print("Hot")
elif 20<=temperature<=30:
    print("Warm")
else:
    print("Cold")