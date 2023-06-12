class SPI:

    def take_value(self):
        principal=int(input("enter a principal:"))
        rate=int(input("enter a rate:"))
        time=int(input("enter a time:"))
        return[principal,rate,time]

    def calculate(self):
        principal,rate,time=self.take_value()
        si=(principal*rate*time)/100
        return si

    def display(self):
        return f"simple intrest is :{self.calculator()}"

    obj=SPI()
    print(obj.display())


