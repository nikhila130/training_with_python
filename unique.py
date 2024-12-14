'''to find the unique element in the given list'''
l=list(map(int,input().split()))
x=0
for i in l:
    x^=i
print(x)

'''using xor we can remove duplicates as it 
cancels equal values so we can find the unique element '''

