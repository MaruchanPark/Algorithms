'''
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가
주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고,
10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
'''

#DFS로 완전탐색하며 최대값, 최소값 갱신

N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int,input().split())

max_ = (1e+10) * -1
min_ = 1e+10

def dfs(depth, val, add, sub, mul, div):
    global max_, min_
    if depth == N:
        max_ = max(val, max_)
        min_ = min(val, min_)
        return

    if add > 0:
        dfs(depth + 1, val + num[depth], add - 1, sub, mul, div)
    if sub > 0:
        dfs(depth + 1, val - num[depth], add, sub - 1, mul, div)
    if mul > 0:
        dfs(depth + 1, val * num[depth], add, sub, mul - 1, div)
    if div > 0:
        dfs(depth + 1, int(val / num[depth]), add, sub, mul, div - 1)


dfs(1, num[0], add, sub, mul, div)

print(max_)
print(min_)
