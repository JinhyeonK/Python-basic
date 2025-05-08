cnt=1
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j!=i:
            print(cnt,end=" ")
            j+=1
            cnt+=1
        else:
            print(cnt)
            cnt+=1

print()