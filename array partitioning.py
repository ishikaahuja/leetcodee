l=[]
sum=0
nl=[]
n=int(input())
if(n%2!=0):
    print("incorrect i/p")
else:
    for i in range(0,n):
        l.append(int(input()))
    l.sort()
    for i in range(0,n,2):
        nl.append(min(l[i],l[i+1]))
    for i in range(0,len(nl)):
        sum=sum+nl[i]
    print(sum)
