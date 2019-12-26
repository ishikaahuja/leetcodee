n=int(input())
i=0
j=0
row=1
count=0
flag=0
while(count<n):
    for i in range(0,row):
        if(count<n):
            print("*",end="")
            
        else:
            print(row-1)
            flag=1
            break
        count=count+1
            
        
    print("\n")
    row=row+1
if(flag!=1):
    print(row-1)

    
    
