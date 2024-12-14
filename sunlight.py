'''we have to give the no.of buildings receiving  the sunlight..
means if there are shorter numbers in the building it wont get sunlight'''

l=list(map(int,input().split()))
max=0
count=0
for i in l:
    if i>max:
        max=i
        count+=1
print(count)