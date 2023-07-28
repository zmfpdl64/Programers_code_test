# 22시 05분 22시 06분
# 브5
# https://www.acmicpc.net/problem/10869
# 시간복잡도 O(1)

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b) # 나머지 버림
print(a%b)