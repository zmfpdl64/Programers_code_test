#11시 19분

# a = list()
# b = dict()
# for i in range(int(input())):
#     a.append(list(input().split()))
# for i in range(len(a)):
#     b[a[i][0]] = []

# for i in range(len(a)):
#     b[a[i][0]].append(a[i][1])

# b = dict(sorted(b.items(), key=lambda x: x[0]))
# for i, v in b.items():
#     for j in range(len(v)):
#         print(i, v[j])

a = list()
b = list()
for i in range(int(input())):
    a.append(list(input().split()))

a = sorted(a, key= lambda x : int(x[0]))
for i in range(len(a)):
    print(a[i][0], a[i][1])