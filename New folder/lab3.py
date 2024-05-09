a =[]
while(True):
    b = int(input())
    if(b != 0):
        a.append(b)
    else:
        break
a.sort()
print(a)