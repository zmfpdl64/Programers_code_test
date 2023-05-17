# 19시 37분
# 19시 56분 29분

def solution(files):
    answer = []
    lists = []
    for idx, file in enumerate(files):
        a = False
        for i in range(len(file) - 1):
            if (not file[i].isalnum() or file[i].isalpha()) and (file[i + 1].isalnum() and not file[i + 1].isalpha()):
                for j in range(i + 1, len(file) - 1):
                    if file[j].isalnum():
                        pass
                    else:
                        lists.append([file[:i + 1], file[i + 1: j], file[j:], idx + 1])
                        a = True
                        break
                else:
                    lists.append([file[:i + 1], file[i + 1:], '', idx])

                if a:
                    break
    lists.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))
    for i in lists:
        answer.append(''.join(i[:-1]))
    return answer