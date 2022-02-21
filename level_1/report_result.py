'''
프로그래머스 문제 신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/92334

'''
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    # dict 자료형이 더 수월할까 아니면 배열에 넣어서 풀까
    # 유저와 유저가 신고당한 횟수, 딱 키값과 value 값을 나눌수 있어서 dict 자료형을 쓰는게 맞는거 같다. 
    # 아니면 유저와 유저를 신고한 사람 수 , 그리고 value 값이 갯수가 k 이상이면 메일
    
    dic_report = {id:[] for id in id_list}
    
    report = set(report) # 중복되는 값을 빼준다. set자료형의 장점이다. 
    
    for i in report: # 파이썬 set 자료형. 중복을 허용하지 않는다. 순서가 없다. 
        report = i.split(' ')
        #print(report)
        dic_report[report[1]].append(report[0])
    
    for key, value in dic_report.items():
        if len(value)>=k:
            for v in value:
                answer[id_list.index(v)]+=1
    return answer