'''
주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 

만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래,
이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다.

입력:
첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며,
1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다.
각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.

출력:
영상을 압축한 결과를 출력한다.

문제링크:
https://www.acmicpc.net/problem/1992
'''

import sys

N = int(input())
map_ = []
for i in range(N):
    map_.append(sys.stdin.readline().rstrip())

def check(x, y, n):
    #입력의 첫 번째 값과 모든 값을 비교
    base = map_[y][x]
    ext_idx = 1
    for i in range(x, x + n):
        for j in range(y, y + n):
            if base != map_[j][i]:
                ext_idx = 0
                break

        if ext_idx == 0:
            break
    #모두 같으면 압축 (출력)
    if ext_idx == 1:
        print(base, end = '')
        return
    #다르면 분할하여 비교
    else:
        print('(', end = '')
        #입력 4분할 위해 범위 설정하여 함수 실행
        x_ = x
        y_ = y
        check(x_, y_, n//2)

        x_ = x + n // 2
        y_ = y
        check(x_, y_, n//2)

        x_ = x
        y_ = y + n // 2
        check(x_, y_, n//2)

        x_ = x + n // 2
        y_ = y + n // 2
        check(x_, y_, n//2)
        print(')', end = '')


check(0,0, N)
