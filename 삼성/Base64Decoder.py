# 17시 40분 18시 33분
T = int(input())
dic = {}
for i in range(26):
    dic[chr(65+i)] = i
for i in range(26):
    dic[chr(97+i)] = 26+i
for i in range(10):
    dic[str(i)] = 52+i
dic["+"] = 62
dic["/"] = 63
for idx in range(1, T+1):
    ins = input().rstrip()
    line = ""
    for s in ins:
        b = bin(dic[s])[2:].rjust(6, "0")
        print(b)
        line += b
    byte = ""
    for i in range(0, len(line)//8):
        byte += chr(int(line[i*8:(i+1)*8], 2))
    print("#{} {}".format(idx, byte))
