class student:
    __name=''
    __password=''

@property
def get_name(self):
    return self.__name
@get_name.setter
def get_name(self,name):
    self.__name=name

@get_name.deleter
def get_name(self):
    del self.__name

def get_password(self):
    return self.__password

@get_name.setter
def get_password(self,password):
    self.__password=password
@get_password.deleter
def get_password(self):
    del self.__password
obj=student()
obj.get_name='ram'
print(obj.get_name)
obj.get_password='ram123'
print(obj.get_password)
del obj.get_name
print(obj.get_name)
