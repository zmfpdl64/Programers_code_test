#1. headgear(x)  2. eyewear(y)  3. face(n), 4. clothes(m)
#1개일 때    x or y or n or m
#2개일 때 x


#4개일 때
#1개만 선택했을 때 x + y + n + m
#2개 선택 x(y+n+m) + y(n+m) + n*m
#3개 선택 x*y(n+m) + x*n*m + y*n*m
#4개 선택 x*y*n*m

def solution(clothes):
    answer = 1
    a = {x[1]: 1 for x in clothes}
    for x in clothes:
        a[x[1]] += 1
    
    for v in a.values():
        answer *= v
    
    answer -= 1
    

    print(answer)

    return answer


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])