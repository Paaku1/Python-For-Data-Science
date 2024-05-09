s = "Hello@gmail.com"
x = []
for i in range(len(s)):
    if(s[i] == '@'):
        i += 1
        while(s[i] != '.'):
            x.append(s[i])
            i += 1        
r = ''.join(x)
print(r)

