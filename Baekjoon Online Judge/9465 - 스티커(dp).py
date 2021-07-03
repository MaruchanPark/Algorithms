'''
문제 - https://www.acmicpc.net/problem/9465

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다.
다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다. 연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다. 

출력
각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.
'''

# 테스트 케이스와 동일한 dp 리스트를 만들고
# i번째 column에 이전에 선택한 스티커의 값들을 더한 최댓값을 저장한다.
# 최댓값의 후보는 다음과 같다
# i-1번째 교차하는 row의 값
# i-2번째 위, 아래 row의 값

# 답은 맞지만, 알고리즘이 비효율적이다. 개선 할 것.

import sys

T = int(input())
for _ in range(T):
    n = int(input())
    steaker = []

    for _ in range(2):
        steaker.append(list(map(int, sys.stdin.readline().split())))

    dp = [[0] * n for _ in range(2)]

    dp[0][0] = steaker[0][0]
    dp[1][0] = steaker[1][0]

    dp[0][1] = dp[1][0] + steaker[0][1]
    dp[1][1] = dp[0][0] + steaker[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1] + steaker[0][i], dp[0][i-2] + steaker[0][i], dp[1][i-2] + steaker[0][i])
        dp[1][i] = max(dp[0][i-1] + steaker[1][i], dp[0][i-2] + steaker[1][i], dp[1][i-2] + steaker[1][i])

    print(max(dp[0][-1], dp[1][-1]))
