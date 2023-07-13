# 22시 23분 22시 ??분
# 실버 4
# https://www.acmicpc.net/problem/1543
# 시간 복잡도 O(n * size)

doc = input()
search_word = input()

idx = 0
size = len(search_word)
count = 0
# 문자열 비교하기
while(idx <= len(doc)-size):
    if doc[idx:idx+size] == search_word:
        count += 1
        idx += size
    else:
        idx += 1
print(count)