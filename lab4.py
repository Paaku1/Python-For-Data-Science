m = input()
if(m == 'January' or m == 'March' or m == 'May' or m == 'July' or m == 'August' or m == 'October' or m == 'December'):
    print(m,"has 31 days")
elif(m == 'April' or m == 'June' or m == 'September' or m == 'November' ):
    print(m,"has 30 days")
elif(m == "February"):
    print(m,"has 28 or 29 days")
else:
    print("-1")
