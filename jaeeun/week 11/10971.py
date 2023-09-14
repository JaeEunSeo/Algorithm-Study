#외판원 순회 2
import sys
input = sys.stdin.readline

N = int(input())
map= [list(map(int, input().split()))for _ in range(N)]
min_cost = 1e9
visited = []

def dfs(start, next, cost, visited):
    global min_cost
    if len(visited) == N:
        if map[next][start] !=0 :
            min_cost = min(min_cost, cost + map[next][start])
            return
    for i in range(N):
        if cost > min_cost:
            continue
        if map[next][i] !=0 and i not in visited and i!=start:
            visited.append(i)
            dfs(start, i, cost + map[next][i], visited)
            # 다음 순회를 위해서 visited 리스트 비워주기
            visited.pop()

for i in range(N):
    dfs(i, i, 0, [i])

print(min_cost)