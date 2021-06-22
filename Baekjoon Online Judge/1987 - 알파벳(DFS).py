'''
문제 https://www.acmicpc.net/problem/1987
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
'''

# Pypy3 제출
#BFS 탐색은 최단거리로 이동하기 때문에, DFS로 탐색해야 하는 문제.
#알파벳을 리스트로 저장해서 체크하면 시간초과가 뜬다.
#알파벳 길이를 늘려가며 dfs 함수의 입력으로 사용, 방문여부 체크

#* ord() 이용, 26 길이의 list로 알파벳의 방문 여부를 체크해도 시간 내에 해결 가능.

#** 재귀함수 dfs 아닌 stack 사용시에 훨씬 빠른 다른 코드들이 확인됨. 직접 구현해보고 설명 추가할 것.

import sys
R, C = map(int, sys.stdin.readline().split())

map_ = []
for i in range(R):
    map_.append(sys.stdin.readline())


def dfs(row,col, alphabet, length, n_move):
    global max_

    max_ = max(max_, length)
    for i in range(4):
        row_ = row + d_row[i]
        col_ = col + d_col[i]

        if 0 <= row_ < R and 0 <= col_ < C and map_[row_][col_] not in alphabet:
            dfs(row_, col_, alphabet + map_[row_][col_], length + 1)

max_ = 0
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

dfs(0,0, map_[0][0], 1)

print(max_)
