# Calculus 1

x = int(input("Enter x = "))
y = int(input("Enter y = "))
#operation = input("Enter operation : ")


### Формальные параметры
def add(a,b):
    """ doc """
    return a + b

def menu():
    print("Select operation : + == Add; - == Substract; * == Multiply; / == Divide")
    return input("Enter choice(+|-|*|/):")

operation = menu()
if operation == '+':
### Фактические параметры
    print("x + y = ", add(x,y))
elif operation == '-':
    print("x - y = ", x - y)
elif operation == '*':
    print("x * y = ", x * y)
elif operation == '/':
    if y != 0:
        print("x / y = ", x / y)
    else:
        print("You've entered some shit!")
else:
    print("You've entered some shit!")



