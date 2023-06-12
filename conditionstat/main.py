#if, else ,elf
x=5
y=10
if x>y :
    print("x is greater than y")
else:
    print("y is greater than x")



x=50
y=300
z=200
if x>y and y>z:
    print("x is greater than y and z")
elif y>x and y>z:
    print("y is greater than x and z")
else:
    print("z is greater than x and y")




x = int(input("enter any  number"))
if x % 3 == 0:
    print(" x is divisible by 3")
elif x % 5 == 0:
    print("x is divisible by 5")
else:
    print("x is not divisible by 3 and 5 ")

num=5
if num % 2 == 0:
    print("even")
else:
    print("odd")


english = input("enter the english")
nepali = input("enter the nepali")
math =input("enter the math")
science = input("enter the science")
computer = input("enter the computer")
total = english + nepali + math + science + computer
percentage = total/5

if percentage >= 35 and percentage <= 45:
    print("third division")
elif percentage >= 45 and percentage <= 60:
    print("second division")
elif percentage >= 60 and percentage <= 75:
    print("first division")
elif percentage >= 75 and percentage <= 100:
    print("distinction")
else:
    print("fail")