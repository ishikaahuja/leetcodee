m=int(input())
bit=[]
flag=0
for i in range(0,m):
    bit.append(int(input()))
for i in range(0,m):
    print(i)
    if(i+1<m and i-1>=0):
        print('level1')
        if(bit[i-1]<bit[i]):
            
            
            if(bit[i+1]<bit[i]):
                
                if(bit[i+1]>bit[i-1]):
                    print("true")
                    flag=1
                    break

               
if(flag!=1):
               print('false')

