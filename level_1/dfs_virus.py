'''
dfs - virus , bfs- virus 
백준 바이러스 문제 
간단한 그래프 탐색문제
근데 구현을 못하겠다.... 
there's many way to implement, i have to choose one.
'''
from collections import deque
n = int(input())# the number of computers
m = int(input())# the number of connections
graph = [[] for _ in range(n+1)] # graph initiation, make list n 
# i have to make graph, what i wanna make,
for i in range(m):
# just wanna repetation, i can use _ instead of i 
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(n+1):
  print(graph[i])


'''
n,m = 7,6
graph = [[],
[2, 5],
[1, 3, 5],
[2],
[7],
[1, 2, 6],
[5],
[4]
]'''
answer = 0
cnt =0 
def dfs(graph,v,visited):
  visited[v] = True
  global cnt
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)
      cnt +=1


def bfs(graph,v, visited):
  queue = deque([v])
  visited[v] = True
  while queue :
    v = queue.popleft()
    print(v,end='  ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
    
visited = [False]*(n+1)
#dfs(graph,1,visited)
bfs(graph,1,visited)
answer = sum(visited)-1
print(visited)
print(answer)
