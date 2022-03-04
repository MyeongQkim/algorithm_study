'''
이코테 삽입 정렬 코드
'''

array = [3,9,6,34,12,77,4,3,1]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j],array[j-1] = array[j-1],array[j]
    else : 
      break

print(array)