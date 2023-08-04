import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

res = []
q = deque(i for i, n in enumerate(indegree) if not n)
while q:
    res.append(now:=q.popleft())
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
print(*res[1:])