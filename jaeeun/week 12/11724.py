import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)


def dfs(start, graph):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, graph)
        else:
            continue


cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, graph)
        cnt += 1

print(cnt)
