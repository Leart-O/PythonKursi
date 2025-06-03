def add(x,y):
    return x+y

def concatenate(x,y):
    return str(x)+ str(y)

def operate(operation, x ,y):
    return operation (x ,y)

result_sum = operate(add, 3 ,2)
result_concatenate = operate(concatenate, "hello " , "idriz")
print(result_sum)
print(result_concatenate)
