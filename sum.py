'''to find the sum of odd numbers present in the even indexes'''


'''l=list(map(int,input().split()))
result=[]
sum=0
for i in l:
    if i%2==0:
        result.append(i)
print(result)
for j in result:
    if j%2!=0:
        sum+=j
print(sum)'''

l=[1,2,3,4,5,6]
s=0
for i in range(len(l)):
    if i%2==0 and l[i]%2!=0:
        s+=l[i]
print(sum)
