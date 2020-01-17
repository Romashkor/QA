import math

print("Hi. This is simple calculation software.")

while True:
    try:
        x = input('Please, indicate your number : ')
        answer = float(x)
        break
    except ValueError:
        print("It was not a number.")

while True:
    try:
        y = int(input("""Please specify what do you want to do with the number :
        1. Calculate sin
        2. Calculate cos
        3. Calculate log
        4. Calculate the square
        : """))
        answer1 = int(y)
        break
    except ValueError:
        print("""It was not a number.""")

while y > 4 or y < 0:
    y = int(input("""Incorrect value. Please specify what do you want to do with the number :
    1. Calculate sin
    2. Calculate cos
    3. Calculate log
    4. Calculate the square
    :"""))

if y == 1:
    print("sin x = ", math.sin(float(x)))
elif y == 2:
    print("cos x = ", math.cos(float(x)))
elif y == 3:
    print("log x = ", math.log(float(x)))
elif y == 4:
    print("x ^ 2 = ", math.pow(float(x),2))