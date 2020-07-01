graph = {1:[2,5],2:[1,3,4],3:[2],4:[2],5:[1,6],6:[5]}
visited = [False]*6
print(visited)

def dfs(at):
    if(visited[at-1]==True):
        return None
    else:
        print("im at,",at)
        visited[at-1]=True
        for c in graph[at]:
            dfs(c)
a = dfs(6)
