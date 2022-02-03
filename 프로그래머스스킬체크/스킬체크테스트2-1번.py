def solution(n, words):
    answer = []
    stack = []
    failer = 0
    for i in range(1, len(words)):
        if words[i][0] == words[i-1][-1]:
            if words[i] in stack:
                failer = i
                break
            else:
                stack.append(words[i-1])
            
            continue
        else:
            failer = i
            break
    if failer == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append((failer)%n +1)
        answer.append(int((failer/n)+1))            

    print(answer)
    return answer


solution(5, 	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])


a = ['list', 'bist']

print(a[0][1])
