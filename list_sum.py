'''l=[1,2,3,4,5,6]
l.sort()
print(l)
sum1=0
for i in range(0,3):
    a=i<l[:4]
sum1=sum1+i
i=i+1
print(sum1)'''

l=[1,3,2,4,5,6]
l.sort()
print(sum(l[:3]))

'''question is to get the sum of minimum 3 elements of list'''