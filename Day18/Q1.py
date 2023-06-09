a=[1,-2,3,-1]
b=[]
c=[]
for i in a:
    if i<0:
        b.append(i)
    else:
        c.append(i)
print(b+c)