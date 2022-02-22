'''
프로그래머스 문제 로또 최고 최저 순위
https://programmers.co.kr/learn/courses/30/lessons/77484

'''

def solution(lottos, win_nums):
    answer = []
    print(lottos)
    min_cnt = 0
    zero_cnt = 0
    for i in lottos:
        for j in win_nums:
            if i == j :
                min_cnt +=1
                print(min_cnt)
    for i in lottos:
        if i == 0:
            zero_cnt +=1
    max_cnt = min_cnt+ zero_cnt
    max_rate = 7-max_cnt
    min_rate = 7-min_cnt
    if max_rate>=7:
        answer.append(6)
    else: answer.append(max_rate)
    if min_rate >=7:
        answer.append(6)
    else: answer.append(min_rate)
    return answer

'''
로또가 당첨될 최고 순위와 최저 순위 

로또에 0이 있는 개수 순서는 상관 없다. 

1. for 문으로 탐색하면서 win nums와 같은 것의 갯수를 센다. 
2. 0이 있을 경우 갯수에 추가를 한다. 
3. max와 min은 max = min + 0 num 이다. 
4. 6개이면 1등 5개이면 2등 6등이면 exception


'''