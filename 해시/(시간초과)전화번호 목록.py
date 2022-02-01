def solution(phone_book):
    answer = True
    
    for i, v in enumerate(phone_book):
        for j in range(i+1, len(phone_book)):
            #print(v, phone_book[j][:len(v)])
            if len(v) <= len(phone_book[j]) and v == phone_book[j][:len(v)]:
                answer = False
                break
    print(answer)
    return answer


solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])
