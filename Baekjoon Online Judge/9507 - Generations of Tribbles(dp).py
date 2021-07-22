'''
문제 - https://www.acmicpc.net/problem/9507

입력
입력의 첫 번째 줄을 테스트 케이스의 개수 t (0 < t < 69)가 주어진다. 다음 t줄에는 몇 번째 피보나치를 구해야하는지를 나타내는 n(0 ≤ n ≤ 67)이 주어진다.

출력
각 테스트 케이스에 대해, 각 줄에 꿍 피보나치값을 출력하라.
'''

# 반복 연산을 막기 위해 최대 값 범위 만큼 리스트를 만들고 저장한다.
# 이미 계산했으면 불러오고, 계산하지 않은 영역이면 계산하여 저장해준다.

N = int(input())
def koong(n):
    if fibo[n]:
        return fibo[n]
    else:
        fibo[n] = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)
        return fibo[n]

fibo = [0] * 68
fibo[0] = 1
fibo[1] = 1
fibo[2] = 2
fibo[3] = 4

for i in range(N):
    n = int(input())
    print(koong(n))
