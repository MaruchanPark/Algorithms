'''
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
'''

import sys
n = int(input())
x = list(map(int,sys.stdin.readline().split()))
xt = list(sorted(set(x))) #중복 제거, 오름차순 정렬
#list xt의 index가 더 작은 값의 갯수가 된다. 값을 key, 갯수를 value로 하는 dictionary 생성
xt = {xt[i]:i for i in range(len(xt))}

#입력 list의 순서대로 dictionary value 출력
print(*[xt[i] for i in x])
