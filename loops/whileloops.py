# x=1
# while x <= 10 :
#     print(x)
#     x+=1



# num=int(input("enter a number:"))
# x=1
# while x<=num:
#     print("hello")
#     x+=1

num=int(input("enter a number:"))
x=1
studentsmark = []
while x<=num:
    print(f"=============student{x}====================")
    for a in range(1):
        nepali=int(input("enter nepali marks:"))
        english=int(input("enter english marks:"))
        science=int(input("enter science marks:"))
        social=int(input("enter social marks:"))
        math=int(input("enter math marks:"))
        total=nepali+english+science+social+math
        studentsmark.append(total)
    x+=1
print(studentsmark)






