# answer [가입자 수, 판매액]
# 1.최저 할인율 부터 점차 올리면서 가입자수를 최대로 늘려본다.
# 2. 더 이상 늘어나지 않으면 판매액을 할인율을 조정하여 판매액을 늘린다.
# 3. 최저 할인율을 시행해도 이모티콘 플러스 서비스 가입자가 없으면 판매액을 늘림
import itertools

# 할인율 : 플러스 가입자 수
# 

def solution(users, emoticons):
    discount = itertools.combinations_with_replacement(range(1, 41), len(emoticons))
    result = []
    answer = []
    for i in discount:
        count = 0
        money = 0
        for j in range(len(users)):
            dis = users[j][0]
            cash = users[j][1]
            for k in range(len(i)):
                if i[k] >= dis: #구매 함
                    print(i[k])
                    use_money = emoticons[k] *(100 - i[k]) * 0.01
                    cash -= use_money
                    money += use_money
                else:
                    pass
            if cash < 0:
                count += 1
        result.append([count, money])
    result = sorted(result, key=lambda x: (-x[0], x[1]))
    # print(result)
    # print(result[0])
            
            

            
    # dis = [ i for i in range(1,41)]
    # dis_sub = {}
    # for i in dis:
    #     count = 0
    #     for j in range(len(users)):
    #         cash = users[j][1]
    #         u_dis = users[j][0]
    #         if u_dis > i:
    #             pass
    #         else:
    #             for k in emoticons:
    #                 cash -= (k * (100 - i)*0.01)
    #             if cash < 0:
    #                 count +=1
    #     dis_sub[i] = count
    # dis_sub = dict(sorted(dis_sub.items(), key =lambda x: (-x[1], x[0])))
    # max_sub = list(dis_sub)[0]
    # print(dis_sub)


    return answer
solution(
[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
solution(
[[40, 10000], [25, 10000]], [7000, 9000])