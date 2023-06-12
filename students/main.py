import os
if not os.path.exists("record.txt"):
    with open("record.txt","w")as f:
        pass

def register():
    print("====================================")
    print("============register================")
    print("====================================")
    username=input('enter a username')
    username=username.strip()
    if username in open('record.txt').read():
        print("username already exists")
        exit()
    # password=input('enter a password')
    # password=password.strip()
    password= getpass.getpass('enter a password:')
    password=password.strip()
    confirm_password=getpass.getpass('confirm password:')
    confirm_password=confirm_password.strip()
    if password!=confirm_password:
        print('password do not match')
        exit()
    with open ('record.txt','a')as f:
        f.write(f"username:{username},password:{password}")
        f.write("/n")
        print("registration sucessful")
register()

def login():
    print("====================================")
    print("============login================")
    print("====================================")
    username=input("enter username:")
    username=username.strip()
    password=getpass.getpass("enter password:")
    password=password.strip()
    with open('record.txt','r') as f:
        login_sucess=false
    for student in f.readlines():
        uname=student.split(',')[0].split(':')[1]
        pword=student.split(',')[1].split(':')[1]
        pword=pword.strip()

    if username==uname and password==pword:
        login_sucess=true
    if login_sucess:
        print(f"welcome{username}")
    else:
        print("invalid username or password")
login()
exit()

question=input("do you have an account?(y/n):")
if question=="y":
    login()
elif question=="n":
    register()
else:
    print("invalid input")