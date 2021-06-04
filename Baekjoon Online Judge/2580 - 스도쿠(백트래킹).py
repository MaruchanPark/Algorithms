'''
문제
게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.

스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.
'''
import sys
#풀이:
#입력에서 0인 부분에 대해서 가로축, 세로축, 3x3 사각형의 값들을 탐색 (dfs)
#1 ~ 9 중에 공통적으로 없는 값으로 수정
#정답이 아닐 경우 0으로 다시 바꾸고 다른 값으로 탐색
#Pyy3 제출
def search_row(row, val):
    if val in map_[row]:
        return False
    return True

def search_column(column, val):
    for i in range(9):
        if map_[i][column] == val:
            return False
    return True

def square(row, column, val):
    x = (column // 3) * 3
    y = (row // 3) * 3

    for dy in range(3):
        if val in map_[y + dy][x:x+3]:
            return False
    return True

def DFS(index):
    if index == len(zero):
        for i in map_:
            print(str(i).strip('[]').replace(',',''))
        sys.exit(0)

    for i in range(1,10):
        col = zero[index][0]
        row = zero[index][1]

        if search_row(row, i) and search_column(col, i) and square(row, col, i):
            map_[row][col] = i

            DFS(index + 1)

            map_[row][col] = 0

map_ = []
for i in range(9):
    map_.append(list(map(int, sys.stdin.readline().split())))

zero = []
for y in range(9):
    for x in range(9):
        if map_[y][x] == 0:
            zero.append((x, y))
DFS(0)
