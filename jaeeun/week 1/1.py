#push -> append
#pop -> pop
#size -> len
#empty -> bool로 판단
#top -> 
import sys
input = sys.stdin.readline
n = int(input())

stack = []

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if not stack :
            print("-1")
        else:
            stack.pop()
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if (stack.empty()): print("1")
        else:print("0")
    elif command[0] == 'top':
        if not stack : print("-1")
        else : print(stack[len(stack)-1])
