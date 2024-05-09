x = 2277
s = set()
l = []
i=0
while(x>0):
    a = x%10
    s.add(a)
    l.append(a)
    x = int(x/10)
    i+=1
r = []
for i in s:
    for  j in l:
        k = 0
        if(s[i] == l[j]):
            k += 1
    r.append(k)
print(r)
print(l)
print(s)