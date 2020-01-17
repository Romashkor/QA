import math


print("Hi. This is simple calculation software.")
x = float(input("Please, indicate your number : "))
#Как проверять тип данных, вводимый пользователем и перезапрашивать в случая введения некорректных ?
#print(bool(str(x)))
#while type(float(x)) != int:# or type(x) != float or type(x) != complex:
#    x = print(input("You've entered text. Please, enter numeric value :"))

y = int(input("""Please specify what do you want to do with the number :
    1. Calculate sin
    2. Calculate cos
    3. Calculate log
    4. Calculate the square
    : """))
while y > 4 or y <= 1:
    y = int(input("""Incorrect value. Please specify what do you want to do with the number :
    1. Calculate sin
    2. Calculate cos
    3. Calculate log
    4. Calculate the square
    :"""))
if y == 1:
    print("sin x = ", math.sin(x))
elif y == 2:
    print("cos x = ", math.cos(x))
elif y == 3:
    print("log x = ", math.log(x))
elif y == 4:
    print("x ^ 2 = ", math.pow(x,2))