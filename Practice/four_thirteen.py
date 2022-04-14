# 4와 13으로 이루어진 숫자 순서대로 배치하기
# 반복문으로 num에 1을 계속 더한다.
# str.count() 함수로 13과 4의 숫자를 세고 길이를 구한다.
# str(num)의 길이와 13과 4로 이루어진 길이가 같으면 조건을 만족하는 값이다.

num = 0
for i in range(5000):
    num += 1
    str_num = str(num)
    n_thirteen = str_num.count("13")
    n_four = str_num.count("4")

    len_num = len(str_num)
    len_unlucky = n_thirteen*2 + n_four

    if len_unlucky == len_num:
        print(num)
