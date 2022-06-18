a = int(input())

grade = list()
grade =list(map(int, input().split()))

maximum = max(grade)
sum = 0
for i in range(a):
    sum += grade[i]/maximum * 100

print("{:.6f}".format(sum / len(grade)))
