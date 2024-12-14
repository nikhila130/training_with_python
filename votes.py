'''
 so we have to take two list which one is the age of voters and
 the other is the candidates votes now we have to get which candidate has more votes and print it


l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1.sort()
print(l3)
count=0
for i in l2:
    if i>18:
        l2.append(i)
print(l2)
for j in l3:
    if l3[i]==l3[i-1]:
        count+=1
print(count)

'''

n=int(input())
votes=list(map(int,input().split()))
age=list(map(int,input().split()))
c=[0]*max(votes)
for i in range(n):
    if age[i]>=18:
        c[votes[i]-1]+=1
'''m=max(c)
print(c.index(m)+1)'''
temp=c.sort(reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0])+1)

