bits=[]
m=int(input())
for i in range(0,m):
    bits.append(int(input()))
k=len(bits)
print(bits[-1])
print(bits[-2])
if (bits[-1]==0):
    print('False')
elif (bits[-1]==0 and bits[-2]==1):
    print('false')
elif (bits[-1]==0 and bits[-2]==0):
    print('true')
    
