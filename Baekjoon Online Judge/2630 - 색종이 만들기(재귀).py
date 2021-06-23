'''
문제 https://www.acmicpc.net/problem/2630
입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다.
색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0,
파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.
'''

# 좌측상단 값과 일치하지 않는 값이 있으면 4등분 해서 4등분의 좌측상단 값과 다시 비교
# 전체 입력에서 시작할 위치를 함수의 입력으로 지정

N = int(input())
paper = []
for i in range(N):
    paper.append(input().split())
n_paper = [0, 0]
def solve(row, col, n):

    split_idx = 0
    for i in range(row, row + n):
        for j in range(col, col + n):
            if paper[i][j] != paper[row][col]:
                split_idx = 1
                break
        if split_idx:
            break

    if split_idx:
        solve(row, col ,n // 2, )
        solve(row, col + n//2 ,n//2, )
        solve(row + n//2, col ,n//2, )
        solve(row + n//2, col + n//2 ,n//2, )

    else:
        n_paper[int(paper[row][col])] += 1

solve(0,0, N)
for i in n_paper:
    print(i)
