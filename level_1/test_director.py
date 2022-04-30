n = int(input())
a= list(map(int,input().split()))
b,c = map(int,input().split())

result = 0 

for student in range(n) :
  if a[student]>0:
    a[student]= a[student]-b
    result +=1
  if a[student]>0:
    result += int(a[student]/c)

    if a[student]%c >0:
      result+=1


print(result)