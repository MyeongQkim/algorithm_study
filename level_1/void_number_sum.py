'''
프로그래머스 문제 없는 수 더하기
https://programmers.co.kr/learn/courses/30/lessons/86051

'''
def solution(numbers):
    answer = -1
    sum = 0
    for i in range(10) : 
        if not  i in numbers:
            sum += i
    
    '''
    for문 2개 돌면서 없는 숫자 찾기 
    '''
    return sum


def solution(numbers):
    return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])

def solution (numbers):
    return 45 - sum(numbers)