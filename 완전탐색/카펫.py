def solution(brown, yellow):
    answer = []
    for i in range(3, 5000):
        for j in range(i, 5000):
            if brown+yellow == i*j and (i-2)*(j-2) == yellow :
                answer.append(j)
                answer.append(i)
                break
        if answer:
            break
    print(answer)
    return answer


solution(10, 2)
solution(8, 1)
solution(24, 24)

# 2x + 2y - 4 = 24  #x + y = 10
# 2(x-2) * 2(y-2) = 24 #(x-2)*(y-2)= 12 # xy - 2(x + y) +4 = 12 # xy - 2(x + y) = 8
# xy = 28
# x + y = 10
# x^2 + 2*xy + y^ = 100
#근의 공식을 이용한 풀이도 가능하다. ax^2 + bx + c 짝수 근의 공식  -b +- 루트(b^2 - ac)   (-b +-루트(b^2 - 4ac))/ 2a 
