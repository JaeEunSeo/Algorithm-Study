#집합

import sys

input = sys.stdin.readline

M = int(input())
S = []

for i in range(M):
    user = input().split()
    cal = user[0]
    all_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if len(user) == 2:
        num = int(user[1])
    if cal == 'add':
        if num not in S:
            S.append(num)
    if cal == 'remove':
        if num in S:
            S.remove(num)
    if cal == 'check':
        if num in S:
            print(1)
        if num not in S:
            print(0)
    if cal == 'toggle':
        if num in S:
            if len(S) == 1:
                S = []
            else:
                S.remove(num)
            continue
        if num not in S:
            S.append(num)
    if cal == 'all':
        S = all_arr
    if cal == 'empty':
        S = []