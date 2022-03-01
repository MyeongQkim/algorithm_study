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
from collections import deque
# 입력 부분 짜기, 2차원 배열 입력하는 방법 까먹지 말자. 
n = int(input())
map = [list(map(int,input().split())) for _ in range(n)]

# visited 만들기 false가 n개인 n개의 2차원 배열 
visited = [[False]*n for _ in range(n)]

print(map)
print(visited)
# 방향 전후 좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# dfs 함수 짜기
def dfs1(x,y):
  if x<=-1 or x>=n or y <=-1 or y>=n:
    return False
  visited[x][y] = 1
  dfs(x-1,y)
  dfs(x,y-1)
  dfs(x+1,y)
  dfs(x,y+1)
  return True
  return False

def dfs(x, y):
    # 집 개수 증가 & 방문체크
    global cnt
    cnt += 1
    visited[x][y] = True
    print(x,y)
    # 인접한 노드 탐색하면서 연결되어 있으면 dfs 재귀호출
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if map[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        
        # 위 아래 왼쪽 오른쪽 탐색
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            # 지도 밖으로 안 나갔는지 확인
            if 0<=nx<n and 0<=ny<n :
                # 집이 있고, 아직 방문한 곳이 아니라면 꼬우
                if map[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt

cnt=0
ans = []
for i in range(n):
  for j in range(n):
    if map[i][j] == 1 and visited[i][j] == False:
      cnt = 0
      dfs(i, j)
      ans.append(cnt)

print(len(ans))
ans.sort()
print('\n'.join(map(str, ans)))