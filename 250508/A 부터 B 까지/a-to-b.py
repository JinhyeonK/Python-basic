A,B=map(int,input().split())
print(A, end=" ")
while True:
    if A<=B:
        if A%2==0:
            A+=3
            if A>B:
                    break
            else:
                    print(A, end=" ")
        else:
            A*=2
            if A>B:
                    break
            else:
                print(A, end=" ")
    else:
        break
        
        