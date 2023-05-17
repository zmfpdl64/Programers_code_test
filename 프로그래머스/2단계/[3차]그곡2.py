# 20시 11분
# 20시 29분

dic = {'A#': 'a', 'B#':'b', 'C#':'c', 'D#':'d', 'F#': 'f', 'G#': 'g'}
def transcode(s):
    for key, value in dic.items():
        s = s.replace(key, value)
    return s
def transtime(s):
    h, m = map(int, s.split(":"))
    return h*60 + m
def solution(m, musicinfos):
    answer = []
    m = transcode(m)
    for music in musicinfos:
        st, ed, title, code = music.split(",")
        code = transcode(code)
        time = transtime(ed)-transtime(st)
        div = time // len(code)
        mod = time % len(code)
        codes = code * div
        if mod != 0:
            codes += code[:mod]
        codes = list(codes)
        if m in ''.join(codes):
            answer.append([title, time])
    if not answer:
        return '(None)'
    return max(answer, key=lambda x: x[1])[0]

c = 'bc'
d = 'cb'
print(c in d)