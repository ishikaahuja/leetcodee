def arithmetic(l):
    diff=[]
    flag=1
    temp=0
    k=len(l)
    for i in range(1,k):
        diff.append(l[i]-l[i-1])
    temp=diff[0]
    for i in range(1,len(diff)):
        if(diff[i]!=temp):
            flag=0
            break
    if(flag==0):
        return 0
    else:
        return 1
    







n=int(input())
series=[]
flag=1
k=3
count=0
if(n<3):
    print("invalid input")
    exit
else:
    for i in range(0,n):
                series.append(int(input()))
    for i in range(0,n):
        k=i+2
        while(k<n):
            l=[]
            for j in range(i,k+1):
                l.append(series[j])
            res=arithmetic(l)
            if(res==1):
                count=count+1
            
            k=k+1
    
    if(n//3>0):
        m=n//3+1
        for i in range(0,n):
            k=i+2*m
            #print(k)
            while(k<n):
                l=[]
                for j in range(i,k+1,m):
                    l.append(series[j])
                res=arithmetic(l)
                if(res==1):
                    count=count+1
                k=k+m
print(count)
    
