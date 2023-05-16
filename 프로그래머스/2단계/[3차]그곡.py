# 18시 47분
# 19시 52분 1시간 5분
def transtime(str1):
    h, m = map(int,str1.split(":"))
    return h*60 + m

def solution(m, musicinfos):
    answer = []
    c = {'A':'A','A#':'a', 'B':'B', 'B#':'b', 'C':'C','C#': 'c','D':'D', 'D#':'d','E':'E', 'F':'F', 'F#':'f','G':'G', 'G#':'g'}
    c = dict(sorted(c.items(), key=lambda x : -len(x[0])))
    for key, value in c.items():
        m = m.replace(key, value)
    for music in musicinfos:
        st, ed, title, code = music.split(",")
        time = transtime(ed) - transtime(st)
        for key, value in c.items():
            code = code.replace(key, value)
        code = list(code)
        line = []
        div = time // len(code)
        mod = time % len(code)
        for i in range(div):
            line += code[:]
        line += code[:mod]
        for i in range(len(line)):
            str1 = ''.join(line)
            if m in str1:
                answer.append([title, time])
    if answer:
        return max(answer, key=lambda x:(x[1]))[0]
    return '(None)'