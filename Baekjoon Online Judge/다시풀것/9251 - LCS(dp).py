'''
문제 - https://www.acmicpc.net/problem/9251
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''

# for 루프 두 개로 문자열을 비교한다.
# 같으면 왼쪽 위의 값에 1을 더해준다.
# 다르면 왼쪽, 위의 값 중 더 큰 값을 택한다.
# 예제에 대하여 DP는 다음과 같다.

#   0 0 0 0 0 0 0
#   0 0 1 1 1 1 1
#   0 1 1 1 2 2 2
#   0 1 2 2 2 3 3
#   0 1 2 2 2 3 3
#   0 1 2 2 2 3 4
#   0 1 2 3 3 3 4

import sys

s_1 = sys.stdin.readline().rstrip()
s_2 = sys.stdin.readline().rstrip()

len_1 = len(s_1)
len_2 = len(s_2)

dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

for i in range(1, len_1 + 1):
    for j in range(1, len_2 + 1):
        if s_1[i-1] == s_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len_1][len_2])
