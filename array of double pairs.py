n=int(input())
l=[]
flag=0
for i in range(0,n):
    l.append(int(input()))
if(n%2!=0):
    print("False")
    exit
else:
    for i in range(0,n):
        comp=l[0]
        if comp/2 in l:
            k=l.index(comp/2)
            print(l.pop(0))
            print(l.pop(k))
            print(l)
        elif comp*2 in l:
            k=l.index(comp*2)
            print(l.pop(0))
            print(l.pop(k-1))
            print(l)
        else:
            break
        if(len(l)==0):
            flag=1
            print("true")
            break
        else:
            flag=0
    if(flag==0):
        print("false")
            











    
    
       
                
