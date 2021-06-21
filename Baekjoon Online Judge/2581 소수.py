'''
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''

#에라토스테네스 체 사용
#최대값까지 True 리스트 만들고
#2부터 N까지 2의 배수를 소수 후보에서 제외
#제외되지 않은 더 큰 숫자들의 배수를 소수 후보에서 제외하기 반복

M = int(input())
N = int(input())

primes = [True] * 10001
primes[1] = False

for i in range(2, N + 1):
    if primes[i] == True:
        for j in range(i + i, N + 1, i):
            primes[j] = False

result = []
for i in range(M, N + 1):
   if primes[i] == True:
       result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
