l = [[2, 3], [1, 2], [4,5], [2,3]]
sorted_l = sorted(l, key=lambda x: (-x[0], -x[1]))
print(sorted_l)