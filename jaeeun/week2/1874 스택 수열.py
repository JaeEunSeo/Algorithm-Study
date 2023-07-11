#스택수열

import sys
n = int(sys.stdin.readline())

stack=[]
result=[]
flag = 0
cur = 1

for i in range(n):
    num = int(sys.stdin.readline())     #수열에 넣고자 하는 수, 해당 수가 나올 때까지 stack에 push함.
    while cur<=num:
        stack.append(cur)
        result.append("+")
        cur+=1      #스택에 오름차순으로 넣고자 하는 수까지 push. 입력한 수를 만나면 while문을 나가게 된다.

    if stack[-1] == num :   #스택의 마지막 값이 넣고자 하는 수와 같을 경우, 스택에서 pop
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag=1
        break

if flag == 0:
    for k in result:
        print(k)
