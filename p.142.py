





import sys

sys.stdin = open('p142.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

print(N, M)
graph = []
visited = [[False]*M for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input())))
print(graph)

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1,y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False
cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
                cnt += 1
print(cnt)
