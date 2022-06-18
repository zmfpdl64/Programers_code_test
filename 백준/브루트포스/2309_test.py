import itertools
 
iterable = [1,2,3,4,5]
result = itertools.permutations( iterable)
for permutation in result:
    print( permutation)