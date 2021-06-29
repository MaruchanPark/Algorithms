# 문제 - https://programmers.co.kr/learn/courses/30/lessons/42627

# 작업시간이 작은 순으로 수행해야 가장 작은 평균을 얻을 수 있다.
# 진행중인 작업이 완료된 시간 이내의 요청 시간 작업들로 최소힙 구성하여
# 요청부터 종료까지 걸린 시간을 계산해 나간다.


import heapq

def solution(jobs):
    answer = 0
    heap = []
    i = 0
    start = -1
    now = 0
    current = 0
    
    while i < len(jobs):
        
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0] 
            answer += (now - current[1])
            i += 1
            
        else:
            now += 1
            
    return int(answer / len(jobs))
