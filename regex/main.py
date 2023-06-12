# message="ram sita gita ram ram sita gita hari madan hari"

# def check_repetition(text):
#     data = {}
#     for word in text.split():
#         if word in data:
#             data[word] += 1
#         else:
#             data[word] = 1
#
#     return data
#
# print(check_repetition(message))





# import re

# password = 'ram6Am'
# password must contain at least one number
# check = re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,16}$", password)
# if check:
#     print("Valid password")
# else:
#     print("Invalid password")



# email validation
# email = input("Enter email: ")
# email must contain @
# email must contain .
# email must contain domain name
# email must contain extension
# email = 'ram@gmail.abc'
# if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$", email):
#     print("Valid email")
# else:
#     print("Invalid email")
# password = input("Enter password: ")
# password must be 5 character long and must contain at least one number

# name = input("Enter name: ")
# name must be string

# if re.search("^[a-zA-Z_]{5}$", name):
#     print("Valid username")
# else:
#     print("Invalid username")
# course = "hello python  7am test 9 python"
# get number
# print(re.findall("\d", course))
# print(re.search("python", course))
# print(re.search("python", course).group())
# print(re.search("h", course).start())
# print(re.search("python", course).end())

# print(dir(re))
