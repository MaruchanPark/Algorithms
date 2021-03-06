'''
문제 - https://www.acmicpc.net/problem/9095
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''

# 1 : 1
# 2 : 1+1, 2
# 3 : 1+1+1, 2+1 1+2, 3
# 4 : [1] 1+1+1+1 1+2+1 1+1+2 1+3,  [2] 2+1+1 2+2,  [3] 3+1
# 4의 [1]은 1에 3의 값을 더했다. [2]는 2에 2의 값을 더했다. [3]은 3에 1의 값을 더했다.
# 5의 경우에는 [1]에 4의 값을 더하고, [2]에 3의 값을, [1]에는 2의 값을 더하면 되므로 7 + 4 + 2 = 13이다.
# 모든 경우에 대해 경우의 수를 구해주고 입력에 맞게 출력한다.

T = int(input())

n_case = [1, 2, 4]
for i in range(3, 10):
    n_case.append(n_case[i-3] + n_case[i - 2] + n_case[i - 1])

for i in range(T):
    n = int(input())
    print(n_case[n-1])
