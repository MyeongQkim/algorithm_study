'''
프로그래머스 문제 완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
'''
'''
def solution(participant, completion):
    answer = ''
    
    participant2 = participant
    for i in participant:
        if i in completion:
            participant2.remove(i)
        else: print(i+" is not in participant")
    answer = participant
    return answer
'''
def solution(participant, completion):
    for p in participant:
        if participant.count(p) > completion.count(p):
                return p

'''
언뜻 보면 문제는 쉬워보이지만 동명이인의 걸러내는것이 키포인트 같다.
숫자를 넣을건지 아니면 제외를 할 건지, 
고민
'''