'''
이코테 선택정렬 코드
'''

array = [3,9,6,34,12,77,4,3,1]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index]>array[j]:
      min_index = j
  array[i],array[min_index] = array[min_index],array[i]

print(array)