#print("=========Computer Bazar=========")
#print("1. Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs:50000)")
#select any option: 1
#enter quantity: ?
#delivery option
#1.Home(Rs:1000) 2.Pickup(Rs:0)
#packing option
#1. Plastic bag(Rs:1000) 2. Bag(Rs:2000) 3. Gift box(Rs:5000) 4.None(Rs:0)
#location:
#1.KTM(13% tax) 2.LTP(0) 3.BKT(0)
#total?
#tax amount?
#grand total?

#answr:

print("=============================")
print("=======computer bazaar=======")
print("1.Dell(Rs.20000 2.Toshiba(Rs.25000) 3.Mac(Rs.50000)")
Dell_price=0
Toshiba_price=0
Mac_price=0
quantity=0
delivery_price=0
packing_price=0
tax_amount=0
total_price = Dell_price +Toshiba_price +Mac_price
options=int(input("enter the options:"))
if options == 1:
    product_name="dell"
    quantity=int(input("enter the quantity:"))
    dell_price=quantity*20000
elif options==2:
    product_name ="toshiba"
    quantity=int(input("enter the quantity:"))
    toshiba_price=quantity*25000

elif options==3:
    product_name ="mac"
    quantity=int(input("enter the quantity:"))
    mac_price=quantity*50000
else:
    print("invalid options")
    exit()

print("========delivery options=========")
print("1.home delivery(Rs.1000) 2.pickup(free)")
delivery_options=int(input("enter a option:"))
if delivery_options==1:
    delivery_price=1000

print ("=======packing option===========")
print("1.plastic bag(Rs.1000)  2.bag(Rs.2000) 3.gift box(Rs.5000) 4.no packing(free)")
packing_options=int(input("entera option:"))
if packing_options ==1:
    packing_price=1000
elif packing_options ==2:
    packing_price=2000
elif packing_options ==3:
    packing_price=5000

print("===========location============")
print("1.kathmandu(13% tax) 2.lalitpur(free) 3.bhaktapur(free)")
location=int(input("enter a option:"))
if location==1:
    tax_amount=total_price*0.13

print("============bill==============")
total_price = Dell_price +Toshiba_price +Mac_price
grand_total=total_price+delivery_price+packing_price+tax_amount
print("product name:",product_name)
print("quantity:",quantity)
print("total price:",total_price)
print("tax amount:",tax_amount)
print("grand total:",grand_total)