n=int(input())
l=[]
k=[]
length=[]
for i in range(0,n):
    
    l.append(int(input()))
for i in range(0,n):
    #print(i)
    j=[]
    j.append(l[i])
    
    flag=0
    while(flag==0):
        if(j[-1]<len(l)):
            
            add=j[-1]
            if l[add] not in j:
                j.append(l[add])
            else:
                flag=0
                break
            
        else:
            flag=0
            break
    k.append(j)
for i in range(0,len(k)):
    length.append(len(k[i]))
no_=length.index(max(length))
print(k[no_])


    

            
        
    
    
