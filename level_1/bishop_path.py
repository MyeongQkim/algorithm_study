'''
코드포스 비숍으로 부터 도망쳐
https://baobab.live/48

'''
bishops = ["D5","E8","G2"]
a = [[0]*8 for _ in range(8)]

print(a)

bmove = [[-1,1],[-1,-1],[1,-1],[1,1]]

for i in bishops :
  x= ord(i[0]) - ord('A')
  y= int(i[1])-1
  a[x][y] =1 
  print (x,y)
  
  for dx,dy in bmove:
    nx,ny = x,y

    while True:
      nx += dx
      ny += dy
      if ny >7 or ny<0 or nx >7 or nx<0:
        break
      a[nx][ny] =1 

print (a)
answer = 0
for x in range(0,8):
  for y in range(0,8):
    if a[x][y]==0:
      answer += 1
      
print (answer)