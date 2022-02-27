'''
dfs - virus , bfs- virus 
백준 단지내 번호붙이기
간단한 그래프 탐색문제

there's many way to implement, i have to choose one.
첫번째 생각 - 그래프 탐색이 연결된 모든 지점을 탐색하는것
그럼 그래프를 어떻게 만들지? 
for 문돌다가 방문하지 않은 좌표를 만나면 새로운 그래프 탐색 시작+1
마지막에 카운트 수, 그래프 탐색 후 탐색한 방문지점의 갯수 리턴
2차원 배열을 어떻게 그래프로 만들지? 그냥 연결된 모든 지점을 왔다갔다 하면서 되는거만 방문기록에 추가? 
1. 우선 입력부분 짜기
2. 입력이 다 되면 visited 만들기
3. 방향에 전후좌우 입력해놓고 모든 노드에 대해서 방문처리가 될수 있도록 진행
4. 탐색하는 방향,bfs 함수 짜기.
  주변 지점 중에서 값이 1이면서 방문처리가 안된 지점 방문
  방문한 지점에서 상하좌우 보면서 다시 방문
5. for문으로 탐색을 진행하며 카운트 할 것들 올려 놓기.


'''

# 입력 부분 짜기, 2차원 배열 입력하는 방법 까먹지 말자. 
n = int(input())
map = [list(map(int,input().split())) for _ in range(n)]

# visited 만들기 false가 n개인 n개의 2차원 배열 
visited = [[False]*n for _ in range(n)]
# 방향 전후 좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# dfs 함수 짜기
def dfs(x,y):
  if x<=-1 or x>=n or y <=-1 or y>=n:
    return False
  visited[x][y] = 1
  dfs(x-1,y)
  dfs(x,y-1)
  dfs(x+1,y)
  dfs(x,y+1)
  return True
  return False

cnt =0 
for i in range(n):
  for j in range(n):
    if dfs(i,j)==True:
      cnt +=1
print(visited)
print(cnt)
  
