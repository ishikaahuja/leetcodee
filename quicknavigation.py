def paths(graph):
    n=len(graph)
    def solve(node):
        if node==n-1:return[[n-1]]
        ans=[]
        for i in graph[node]:
            for path in solve(i):
                ans.append([node]+path)
        return ans
    return solve(0)
k=int(input("enter no. of levels"))
graph=[]
for i in range(0,k):
    sub=[]
    t=1
    print("enter 0 for end of list")
    while(t!=0):
        t=int(input())
        if(t!=0):
            sub.append(t)
            t=1
        else:
            t=0

        
        
    graph.append(sub)
graph.append([])
print(graph)
print(paths(graph))
    
