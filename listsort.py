'''question is to sort the even elements of list in descending order and odd ones in ascending order'''

'''
l=list(input().split())
print(l.sort())
a=[]
b=[]
c=[]
for i in l:
    if i%2==0:
        a.append[i]
    else:
        b.append[i]

a.sort()
b.reverse()
c=a+b
print(c)'''

''''
ALGORITHM:
l.sort()
for i in l:
if i%2!=0:
res.append(i)
else:
res.insert(0,i)
print(res)
'''

l=list(input().split())
res=[]
l.sort()
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)
