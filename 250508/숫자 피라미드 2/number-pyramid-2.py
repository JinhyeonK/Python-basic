cnt=0
n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        if j!=i:
            print(j,end=" ")
            j+=1
        else:
            print(j)
print()