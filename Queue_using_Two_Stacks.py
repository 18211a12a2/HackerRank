x=[]
for t in range(int(input())):
    l=list(map(int,input().split()))
    if l[0]==1:
        x.append(l[1])
    elif l[0]==2:
        x.pop(0)
    else:
        print(x[0])
        