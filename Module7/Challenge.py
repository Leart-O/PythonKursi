#Create a function that takes 3 arguments: number1, number2 and operator.
from Module7.ErrorHandlling import resultati


def calculate(nr1,nr2,operatori):
    #2.  Inside the function, use if-elif-else statements to check the operation and perform the corresponding arithmetic.
    if operatori=="+":
        return nr1+nr2
    elif operatori=="-":
        return nr1-nr2
    elif operatori=="*":
        return nr1*nr2
    elif operatori=="/":
        return nr1/nr2
    else: #3.  Raise a ValueError if the operation is invalid.
        raise ValueError("Invalid operation")

#4.  Outside the function, prompt the user to enter two numbers using input() and convert them to floats.
try:
    num1=float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operatori=input("Enter an operation:+,-,*,/")
    #6.  Call the function with the numbers and the operation.
    resultati=calculate(num1,num2,operatori)
    #7.  Print the result of the operation.
    print(f"The result of {num1} {operatori} {num2}:{resultati}")
# 8.  Use try-except to handle the following exceptions:
# a.  ValueError for invalid input or operation.
except ValueError as e:
    print(f"Invalid input {e}")
# b.  ZeroDivisionError for division by zero.
except ZeroDivisionError as e:
    print(f"Cannot divide by 0 {e}")
# c.  A general Exception for any other unexpected errors.
# d.  Ensure the program prints appropriate error messages for each exception.
except Exception as e:
    print(f"Error: {e}")
#9.  Use a finally block to print a message indicating the end of the program.
finally:
    print("End of the program")

