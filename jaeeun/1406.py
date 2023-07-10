import sys

#편집기에 입력되어 있는 문자열
stack1 = list(sys.stdin.readline().rstrip())
stack2 = []
#반복횟수
n = int(sys.stdin.readline())

#커서를 스택으로 구현함
index = len(stack1)

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if stack1 : stack2 + (stack1.pop())
        else: continue
    if command[0] == 'D':
        if stack2 : stack1 + (stack2.pop())
        else: continue
    if command[0] == 'B':
        if stack1 : stack1.pop()
        else: continue
    if command[0] == 'P':
        if stack1: stack1 = command[1]

stack1 = stack1 + reversed(stack2)
print(''.join(stack1))
        