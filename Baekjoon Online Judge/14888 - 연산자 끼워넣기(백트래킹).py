'''
문제 https://www.acmicpc.net/problem/14888
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데,
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고,
10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
'''

# DFS로 모든 경우 탐색
# 연산의 갯수가 주어지므로 연산 갯수를 입력으로 받는 재귀함수 형태로 구현

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_ = -1e+9
min_ = 1e+9

def dfs(num, depth, add, sub, mul, div):
    global max_, min_
    if depth == N:
        max_ = max(num, max_)
        min_ = min(num, min_)
        return

    if add > 0:
        dfs(num + A[depth], depth + 1, add-1, sub, mul, div)
    if sub:
        dfs(num - A[depth], depth + 1, add, sub-1, mul, div)
    if mul > 0:
        dfs(num * A[depth], depth + 1, add, sub, mul-1, div)
    if div:
        if num < 0:
            dfs((-num // A[depth]) * -1, depth + 1, add, sub, mul, div - 1)
        else:
            dfs(num // A[depth], depth + 1, add, sub, mul, div - 1)

dfs(A[0], 1, add, sub, mul, div)
print(max_)
print(min_)
