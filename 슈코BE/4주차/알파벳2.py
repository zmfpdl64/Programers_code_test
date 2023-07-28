# 1. input값 어떻게 받을거지??
ins = list(input())
# 아스키 코드
alpha_map = [] # 26칸을 가지고 있는 리스트
# 전처리 작업(자료형 생성)
for i in range(26):
    alpha_map.append(0)
# range(0, 8) -> [0,1,2,3,4,5,6,7]
# b a e k j o o n
for i in range(len(ins)):
    alpha = ins[i]
    alpha_map[ord(alpha) - ord('a')] += 1
print(*alpha_map)

# print(" ".join(map(str, alpha_map[97:97+26])))


def solution():
    print("hello")

# 3. 어떤 자료형 사용할거지??
# 4. 알고리즘 할꺼지??

# 2. 출력은 또 어떻게??
