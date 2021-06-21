'''
문제 https://www.acmicpc.net/problem/2798

입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
'''

#브루트포스 문제. 다 더해보고 M을 넘지 않는 최대값을 출력한다.

N, M = map(int, input().split())
nums = list(map(int,input().split()))

max_ = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and i != k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ > max_ and sum_ <= M:
                    max_ = sum_

print(max_)
