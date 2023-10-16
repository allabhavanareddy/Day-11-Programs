'''n=int(input())
w=int(input())
weight=list(map(int,input().split()))
profit=list(map(int,input().split()))
perkg=[]
for i in range(len(weight)):
    perg.append(profit[i]/weight[i])
l=zip(weight,profit,perkg)
l=list(zip(weight,profit,perkg))
l.sort(key=lambda x:x[2])
l.sort(key=lambda x:x[2],reverse=True)#sorts in descending
print(list(l))'''

n=int(input())
w=int(input())
weight=list(map(int,input().split()))
profit=list(map(int,input().split()))
l=list(zip(weight,profit))
l.sort(key=lambda x:x[1]/x[0],reverse=True)#sorts according to profits withot displaying profits
#print(list(l))
maxpr=0
for weight,profit in l:
    if weight<=w:
        maxpr+=profit
        w-=weight
    else:
        maxpr+=w*(profit/weight)
        break
print(maxpr)
    




 








