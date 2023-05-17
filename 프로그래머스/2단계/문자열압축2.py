# 18시 38분
# 19시 26분

def solution(s):
    answer = float('inf')
    for i in range(1,len(s)+1):
        div = len(s)//i
        mod = len(s) % i
        s1 = ''
        m = 0
        for j in range(0, len(s)+1-i, i):
            if m <= j:
                s2 = s[j:j+i]
                cnt = 1
                for k in range(j+i, len(s)+1 - i, i):
                    s3 = s[k:k+i]
                    if s2 == s3:
                        cnt +=1
                    else:
                        break
                if cnt > 1:
                    s1 += str(cnt) + s2
                    m = j + (i*cnt)
                else:
                    s1 += s2
        if mod != 0:
            s1 += s2[-mod:]
        answer = min(answer, len(s1))
    return answer