'''l=[1,2,2,1,3,1,3,3,3,4,5,5,6,4,6]
print(l)
l1=l.sort()
print(l1)
l2=l.count(l)
if l2%2==0:
    print(l)
else:
    print(l)'''

l=[1,3,3,2,3,2,4,5,4,6,5,5]

result=[]
for i in l:
    if l.count(i)%2==0 and i not in result:
        result.append(i)
print(result)

'''question is to consider the list of elements and print those which are repeated even no.of times'''