a = [[False]*3 for _ in range(3)]    #행이 복사가 되서 하나의 행의 요소를 변경하면 모든 행의 수정된다.

# for i in a:
#     print(i)
# a[1][1] = True
# for i in a:
#     print(i)
#     print(i[1:])
# sum = 1
# for i in range(1, int(input())):
#     sum *= i
# print(sum)
int(input())
a = list(map(int,input().split()))
n = int(input())
print(a.count(n))
