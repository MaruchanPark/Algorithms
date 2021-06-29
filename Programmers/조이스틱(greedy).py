# 문제 - https://programmers.co.kr/learn/courses/30/lessons/42860

# 알파벳 이동횟수는 ord()를 이용, A Z와의 값 차이를 이용해서 결정
# 커서를 한쪽 방향으로 이동하다가 반대로 돌아가야 빠른 경우가 있다.
# 커서를 이동할 때 마다 양쪽 방향을 다 고려하여 최소값을 선택하게 한다.

def solution(name):
    
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    
    while True:
        answer += change[idx]
        change[idx] = 0
        
        if sum(change) == 0:
            return answer
        
        right, left = 1, 1
        while change[idx + right] == 0:
            right += 1
        while change[idx - left] == 0:
            left += 1
            
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right
