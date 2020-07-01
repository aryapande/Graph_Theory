graph = {1:[2,5],2:[1,3,4],3:[2],4:[2],5:[1,6],6:[5]}
visited = [False]*6
print(visited)
queue = []
start = 1
queue.append(start)
visited[start-1]=True
while(queue):
    node = queue.pop(0)
    print(node)
    for x in graph[node]:
        if(visited[x-1]==False):
            
            queue.append(x)
            visited[x-1]=True
