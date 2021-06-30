'''
문제 - https://www.acmicpc.net/problem/9663
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

# 재귀 함수의 입력으로 row에 1씩 더해가며 탐색
# column에서 어디에 둘지를 선택할 때, 퀸이 있는 row, 대각 성분을 피해서 두면 된다.
# 두 대각 방향 성분의 갯수는 (N-1)*2 에 가운데 성분 1개의 합이다.
# 좌측 아랫방향 대각성분의 위치는 row + column 인덱스로 결정되고 우측 아랫방향은 row - column + (N-1)로 결정된다.

N = int(input())

up_down = [0] * N
left_down = [0] * (2 * (N-1) + 1)
right_down = [0] * (2 * (N-1) + 1)

n_case = 0

def queen(row):
    global N, n_case

    if row == N:
        n_case += 1

    for col in range(N):
        if up_down[col] == 0 and left_down[row + col] == 0 and right_down[row - col + (N-1)] == 0:

            up_down[col] = 1
            left_down[row + col] = 1
            right_down[row - col + (N-1)] = 1

            queen(row + 1)

            up_down[col] = 0
            left_down[row + col] = 0
            right_down[row - col + (N-1)] = 0

queen(0)
print(n_case)
