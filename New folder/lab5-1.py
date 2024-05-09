x = int(input("Enter: "))
l = []
i = 1
while(i<x):
    if(x%i == 0):
        l.append(i)
    i+=1 
if(sum(l)==x):
    print("True")
else:
    print("false")