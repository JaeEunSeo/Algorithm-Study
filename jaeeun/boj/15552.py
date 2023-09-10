import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    k = input().split()
    print(int(k[0])+int(k[1]))