#9시 50분 9시 54분

a=[]
[a.append(b) if b else a.pop() for b in map(int,[*open(0)][1:])]
print(sum(a))

# n = int(input())
# a = []
# for i in range(n):
#     b = int(input())
#     if b == 0 and len(a) != 0:
#         a.pop()
#     else:
#         a.append(b)
    
# print(sum(a))