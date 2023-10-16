n=int(input())
sum=int(input())
res=0
l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==sum:
               res=1
               print(l[i],l[j],l[k])
               break
if res==0:
    print("not found")
    