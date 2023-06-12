# functions

# def welcome():
#     print("welcome to python")
# welcome()
# welcome()



# def welcome(name):
#     print(f"welcome to python {name}")
#
# welcome ("python")
# welcome ("java")



# def welcome(name,price):
#     print(f"welcome to  {name} and price is {price}")
#
# welcome("python",1000)
# welcome("java",2000)



# def welcome (name="python"):
#     print(f"welcome to {name}")
# welcome()



# def welcome(name="python"):
#     print(f"welcome to {name}")
#
# welcome("java")


# def welcome(name ,price=1000):
#     print(f"welcome to {name} and price is {price}")
#
# welcome("python")



# def welcome (course):
#     print(course)
#
# welcome(["python","java" ,"c++"])


# def welcome (*course):
#     print(course)
# welcome("python","java","c++")



# def welcome(*args, **kwargs):
#  print(args)
#  print(kwargs)
# welcome('python', 'java', 'c++', 'nodejs', name='python', price=1000)



# def welcome():
#  return 'welcome to python'
# print(welcome())


# def add_sub(a, b):
#  c = a + b
#  d = a - b
#  return [c, d]
#
# print(add_sub(10,5))



# def welcome():
#  return "hello"
# print(welcome())


x = 10
# def test():
#  print(x)
# test()



# def test():
#  x = 10
#  print(x)
# test()
# x = 10



# def test():
#  global x
#  x = x + 90
#  print(x)
# test()
# print(x)



# lambda function: anonymous function
# a = lambda x, y: x + y
# print(a(10, 20))



# def test():
#  print("Hello World")
#  test()
#
# test()


# def fac(n):
#  if n == 1:
#  return 1
#  else:
#  return n * fac(n - 1)
#
# print(fac(6))



#simple intrest calculation from ptr??????
# def take_value():
#     p=int(input("enter the principal amount:"))
#     t=int(input("enter the time:"))
#     r=int(input("enter the rate:"))
#     return[p,t,r]
# def calculator():
#     p,t,r =take_value()
#     return p*t*r/100
# def display():
#     return f"simple intrest is {calculator()}"
#
# print(display())




# built a total of 1,2,3,4,5,6,7,8,9  ?????
# def total(*args):
#     sum_number=0
#     for i in args:
#         sum_number=sum_number+i
#     return sum_number
# print(total(1,2,3,4,5,6,7,8,9))




#WAP to enter any data and return the data type
# def data_type(data):
#     return type(data)



#built a function to find the total even and total odd number 1,2,3,4,5,6,7,8,9  ?????
# def even_odd(*args):
#     even=0
#     odd=0
#     for i in args:
#         if i%2 ==0:
#             even=even+1
#         else:
#             odd=odd+1
#         return f"even:{even} odd:{odd}"
# print (even_odd(1, 2, 3 , 4, 5, 6, 7, 8, 9))
#the other way to do:
# data=[]
# for a in range (1,5):
#     data.append(int(input("enter a number:")))
#
# print(even_odd(data))



# def connection():
#     """
#     This function connect database
#     :return
#     """
#     return "database connected"
# print(connection())
#
# print(connection.__doc__)
# print(connection.__name__)
# print(__file__)



