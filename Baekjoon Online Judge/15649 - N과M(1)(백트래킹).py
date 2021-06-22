'''
문제 https://www.acmicpc.net/problem/15649
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

# 완전 탐색 문제
# 방문한 곳을 표시하면서 방문할 수 있는 모든 곳을 탐색, 값을 리스트에 추가
# M회 탐색하면 리스트의 값을 출력한다


N, M = map(int, input().split())

nums = [i for i in range(1,N + 1)]
visited = [False] * N
result = []
def dfs(depth):

    if depth == M:
        for num in result:
            print(num, end = ' ')
        print('')
        return

    for i in range(N):
        if visited[i] == False:
            result.append(nums[i])
            visited[i] = True
            dfs(depth + 1)
            result.pop()
            visited[i] = False

dfs(0)
