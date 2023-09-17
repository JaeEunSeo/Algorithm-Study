import sys

input = sys.stdin.readline

N = int(input())

visited = [False for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
min_cnt = 100


def dfs(start, idx):
    global min_cnt
    if start == N / 2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += graph[i][j]
                elif not visited[i] and not visited[j]:
                    B += graph[i][j]
        min_cnt = min(abs(A - B), min_cnt)
        return

    for i in range(idx, N):
        visited[i] = True
        dfs(start + 1, i + 1)
        visited[i] = False


dfs(0, 0)
print(min_cnt)
