n=int(input())
series=[]
flag=1
if(n<3):
    print("invalid input")
    exit
else:
    for i in range(0,n):
        series.append(int(input()))
    difference=[]
    for i in range(1,n):
        difference.append(series[i]-series[i-1])
    temp=difference[0]
    for i in range(1,n-1):
        if(temp!=difference[i]):
            flag=0
            break
    if(flag==0):
        print("not arithmetic")
    else:
        print("arithmetic")
