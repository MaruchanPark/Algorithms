'''
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다.
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.


입력:
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력:
문제의 조건을 만족하는 쌍의 개수를 출력한다.
'''

# 풀이1
n = int(input())
#seq = set(map(int,input().split()))
seq = list(map(int,input().split()))
x = int(input())

seq.sort()#이분탐색을 위해 오름차순 정렬

left = 0
right = n - 1
n_match = 0

#왼쪽, 오른쪽 탐색을 이동하면서 만날 때 까지 비교
while left < right:
    x_ = seq[left] + seq[right]

    if x == x_:
        n_match += 1
        left += 1
    elif x_ > x:
        right -= 1
    else:
        left += 1
print(n_match)


# 풀이2
n = int(input())
# set로 입력 저장
seq = set(map(int,input().split()))
x = int(input())

n_x = 0

for i in seq:
    target = x-i
    if target in seq:# list일 경우 연산시간 O(N), set일 경우 O(1)
        n_x += 1

print(n_x//2)
