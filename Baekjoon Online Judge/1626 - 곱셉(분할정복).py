'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''

A,B,C = map(int, input().split())

bin_B = bin(B)[2:]

length = len(bin_B)

result = 1
power = [0] * length
power[0] = A
for i in range(1, length):
    power[i] = power[i - 1] * power[i - 1] % C


for i in range(length):
    idx = length -1 - i

    if bin_B[idx] == '1':
        result *= power[i]
        result %= C

print(result)
