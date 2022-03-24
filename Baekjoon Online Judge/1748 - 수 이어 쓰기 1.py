'''
문제 https://www.acmicpc.net/problem/1748
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

1234567891011121314151617181920212223...

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.
'''

# 1. N 보다 낮은 자릿수 까지의 길이 합 계산
# 2. N 자릿수의 N 까지의 길이 합 계산
# 3. 1,2를 합하고 출력

last_number = int(input())

last_magnitude = len(str(last_number))

magnitude_sum = 0
n_partials = 0
for i in range(last_magnitude-1, 0, -1):
    n_partial = 10**(i-1) * 9
    partial_magnitude_sum = n_partial * i
    magnitude_sum += partial_magnitude_sum

    n_partials += n_partial

if last_magnitude > 1:
    last_magnitude_sum = (last_number - n_partials) * last_magnitude
else:
    last_magnitude_sum = last_number * last_magnitude

magnitude_sum += last_magnitude_sum
print(magnitude_sum)
