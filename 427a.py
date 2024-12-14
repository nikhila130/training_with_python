n=int(input())
l=list(map(int,input("enter values:").split()))
unsolved=0
police=0
for e in l:
    if e==-1:
        if police>0:
            police-=1
        else:
            unsolved+=1
    else:
        police+=e
print(unsolved)       