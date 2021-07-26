'''
문제 - https://www.acmicpc.net/problem/10164

입력
입력의 첫째 줄에는 격자의 행의 수와 열의 수를 나타내는 두 정수 N과 M(1 ≤ N, M ≤ 15), 그리고 ○로 표시된 칸의 번호를 나타내는 정수 K(K=0 또는 1 < K < N×M)가 차례로 주어지며, 각 값은 공백으로 구분된다. K의 값이 0인 경우도 있는데, 이는 ○로 표시된 칸이 없음을 의미한다. N과 M이 동시에 1인 경우는 없다.

출력
주어진 격자의 정보를 이용하여 설명한 조건을 만족하는 서로 다른 경로의 수를 계산하여 출력해야 한다. 
'''

# 왼쪽, 위쪽의 이동 횟수를 합한 것이 i, j 번째 격자의 이동 횟수가 된다.
# K 까지 이동 횟수를 합하고, K부터 N-1, M-1 번째 격자까지 합하면 정답이 된다.

N, M, K = map(int, input().split())

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1

if K > 0:
    k_i = (K-1) // M
    k_j = K - (k_i)*M - 1

    for i in range(k_i + 1):
        for j in range(k_j + 1):
            if 0 <= i - 1:
                dp[i][j] += dp[i-1][j]
            if 0 <= j - 1:
                dp[i][j] += dp[i][j-1]
else:
    k_i = 0
    k_j = 0

for i in range(k_i, N):
    for j in range(k_j, M):
        if k_i <= i - 1:
            dp[i][j] += dp[i-1][j]
        if k_j <= j - 1:
            dp[i][j] += dp[i][j-1]

print(dp[N-1][M-1])
