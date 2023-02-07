#12시 02분 12시 18분 bfs로는 해결했지만 시간초과
#골드5
#처음에서 끝으로 가는 알고리즘도 있지만
#끝에서 처음으로 가는 알고리즘을 이용해야할 때도 있다.

text = input()
answer = input()

while(len(answer) != len(text)):
    a = answer[-1]
    if a == 'A':
        answer = answer[:-1]
    else:
        answer = answer[::-1][1:]
if answer == text:
    print(1)
else:
    print(0)
