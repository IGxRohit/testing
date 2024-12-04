import time

a=time.strftime('%H')
if int(a)<=12:
    print("GOOD Morning buddy")
elif int(a)<=17:
    print("GOOD AFTERNOON")
else:
    print("GOOD Evening")

