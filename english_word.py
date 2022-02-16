'''
프로그래머스 문제 문자열과 영단어 
https://programmers.co.kr/learn/courses/30/lessons/81301

'''
s = "1zerotwozero3"
answer = 0
num_list = []
num_string = ""
cnt = 0 
print (s[cnt])
'''
if s[cnt] == "z":
  cnt +=4
  num_list.append("0")
  num_string = num_string +"0"
elif s[cnt] == "o":
  cnt +=3
  num_list.append("1")
  num_string = num_string +"1"
if s[cnt].isdigit() == True :
  num_list.append(s[cnt])
  num_string = num_string +s[cnt]
  cnt +=1
if s[cnt] == "s":
  if s[cnt+1] == "i":
      cnt +=3
      num_string = num_string +"6"
  if s[cnt+1] == "e":
      cnt +=5
      num_string = num_string +"7"
if s[cnt] == "e":
  cnt +=5
  num_string = num_string +"8"
print(num_list)
print(num_string)
print (cnt)
print(len(s))
answer = int(num_string)
'''
while True :
        if cnt == len(s):
            break
        elif s[cnt].isdigit() == True :
            num_string = num_string +s[cnt]
            cnt +=1
        elif s[cnt] == "z":
            cnt +=4
            num_string = num_string +"0"
        elif s[cnt] == "o":
            cnt +=3
            num_string = num_string +"1"
        elif s[cnt] == "t":
            if s[cnt+1] == "w":
                cnt +=3
                num_string = num_string +"2"
            elif s[cnt+1] == "h":
                cnt +=5
                num_string = num_string +"3"
        elif s[cnt] == "f":
            if s[cnt+1] == "o":
                cnt +=4
                num_string = num_string +"4"
            elif s[cnt+1] == "i":
                cnt +=4
                num_string = num_string +"5"
        elif s[cnt] == "s":
            if s[cnt+1] == "i":
                cnt +=3
                num_string = num_string +"6"
            elif s[cnt+1] == "e":
                cnt +=5
                num_string = num_string +"7"
        elif s[cnt] == "e":
            cnt +=5
            num_string = num_string +"8"
        elif s[cnt] == "9":
            cnt +=4
            num_string = num_string +"9"
        
answer = int(num_string)

print (answer)

'''
another solution


'''