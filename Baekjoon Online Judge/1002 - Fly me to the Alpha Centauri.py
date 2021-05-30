T = int(input())
for t in range(T):
    a,b = map(int,input().split())

    D = b-a
    N = 0
    sum_ = 0
    idx = 0

    for i in range(1,50000):
        sum_ += i*2
        idx += 2
        if sum_ - i*2 < D <= sum_:
            if D > sum_-i:
                N = idx
            else:
                N = idx - 1
            break

    print(N)
