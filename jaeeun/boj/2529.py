#부등호

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
signs = input().split()
z_ = [0,1,2,3,4,5,6,7,8,9]
nums = permutations(z_,N+1)
answer_list = []
answers = []
for lst in nums:
    is_answer = True
    for i in range(len(signs)):
        if signs[i] == '<':
            if lst[i] < lst[i+1]:
                continue 
            else:
                is_answer = False
                break
        if signs[i] == '>':
            if lst[i] > lst[i+1]:
                continue
            else:
                is_answer = False
                break
    if is_answer:
        answer = ''.join(map(str, lst))
        answers.append(answer)


print(max(answers))
print(min(answers))