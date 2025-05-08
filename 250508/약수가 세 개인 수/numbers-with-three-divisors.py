start, end = map(int, input().split())

# Please write your code here.
cnt2=0
for i in range(start,end+1):
    cnt1=0
    for j in range(1, i+1):
        if i%j == 0:
          cnt1+=1
    if cnt1==3:
        cnt2+=1
print(cnt2)