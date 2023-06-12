#100m
#1-10
#ntc to ntc: 2.5
#ntc to ncell: 5
#ncell to ncell: 10
#ncell to ntc: 1.5

#answer:

print("==============================")
print("============price=============")
print("1.ntc to ntc(Rs.2.5) 2.ntc to ncell(Rs.5) 3.ncell to ncell(Rs.10) 4.ncell to ntc(Rs.1.5)")
options=int(input("enter an options:"))
if options == 1:
    network="ntc to ntc"
    duration=int(input("enter the duration:"))
    ntc_ntc=duration*2.5
elif options == 2:
    network="ntc to ncell"
    duration=int(input("enter the duration:"))
    ntct_ncell=duration*5
elif options == 3:
    network="ncell to ncell"
    duration=int(input("enter the duration:"))
    ncell_ncell=duration*10
elif options == 4:
    network="ncell to ntc"
    duration=int(input("enter the duration:"))
    ncell_ntc=duration*1.5
else:
    print("invalid options")
    exit()