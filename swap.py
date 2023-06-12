x=int(input("enter x:"))
y=int(input("enter y:"))
if x>y:
    print(x)
    print(y)
else:
    print(y)
    print(x)


x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))
if x>y:
    if x>z:
        print(x,y,z)
    else:
        print(z,x,y)
else:
    if y>z:
        print(y,z,x)
    else:
        print(z,y,x)


