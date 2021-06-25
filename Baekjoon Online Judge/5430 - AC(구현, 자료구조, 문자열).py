'''
문제 https://www.acmicpc.net/problem/5430
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
'''

# 함수의 실행을 직접하면 시간초과가 뜬다.
# 함수 D는 항상 배열의 최외곽 값을 제거하므로, 출력해야 할 배열의 인덱스만 계산해서 출력한다.

import sys

N = int(input())
for i in range(N):
    orders = sys.stdin.readline().rstrip()
    orders = orders.replace('RR', '')
    n = int(input())
    nums = sys.stdin.readline().strip()[1:-1].split(',')

    start = 0
    end = n
    r_idx = 1
    while orders and start <= end:
        if orders[0] == 'R':
            r_idx *= -1
            orders = orders[1:]

        elif orders[0] == 'D' and r_idx == 1:
            start += 1
            orders = orders[1:]

        elif orders[0] == 'D' and r_idx == -1:
            end -= 1
            orders = orders[1:]

    if orders or start > end:
        print('error')

    else:
        result = nums[start:end]
        if r_idx == -1:
            result.reverse()
            print('['+','.join(result) + ']')

        else:
            print('['+','.join(result) + ']')
