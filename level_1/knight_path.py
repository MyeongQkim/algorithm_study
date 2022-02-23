'''
이코테 완전탐색 유형 - 왕실의 나이트


'''

input_data = input()
row = int(intput_data[1])
column = int(ord(input_data[0]))- int(ord('a'))+1

# 나이트가 이동할수 있는 방향 정의 

steps = [(-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0 
for step in steps:
  next_row = row +step[0]
  next_column = column+step[1]

if next_row >= 1 and next_row <= 8 and next_column>=1 and next_column <=8:
  result +=1

print(result)