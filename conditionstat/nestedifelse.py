x=50
y=200
z=300
if x>y:
    if x>z:
        print("x is greater:")
    else:
        print("z is greater:")
else:
    if y>z:
        print("y is greater:")
    else:
        print("z is grater:")





#age: 18<  >40 , 18-25 beer 25-40 wine
#nested if else :

x=int(input("enter your age"))
if x>18:
    if x>40:
        print("not allowed to the party[overage]")

    else:
        print("allowed to the party")

    if x<=25:
        if x>=25:
            print("you can have beer")

        else:
            print("you can have wine")
else:
    print("you are underage")


