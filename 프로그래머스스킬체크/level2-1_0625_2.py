import itertools
from math import factorial
def solution(n, k):
    a = [i for i in range(1, n+1)]        
    result = list(itertools.permutations(a, 1))
    print(result)
    
print(factorial(20))
solution(4, 5)