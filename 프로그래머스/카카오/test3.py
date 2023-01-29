# answer [가입자 수, 판매액]
# 1.최저 할인율 부터 점차 올리면서 가입자수를 최대로 늘려본다.
# 2. 더 이상 늘어나지 않으면 판매액을 할인율을 조정하여 판매액을 늘린다.
# 3. 최저 할인율을 시행해도 이모티콘 플러스 서비스 가입자가 없으면 판매액을 늘림


# 할인율 : 플러스 가입자 수
# 

def solution(users, emoticons):
    answer = []
    dis = set([i[0] for i in users])
    dis_sub = {}
    print(dis)

    # users = list(sorted(users, key = lambda x : x[0] ))
    for i in dis:
        count = 0 #가입자 수
        for j in range(len(users)):
            cash = users[j][1]
            u_dis = users[j][0]
            if u_dis <= i:  #할인율이 더 낮을 경우
                pass
            else:           #할인율 충족 했을 경우
                for k in emoticons:
                    cash -= k * i
                if cash < 0:
                    count += 1
        dis_sub[i] = count
    dis_sub = dict(sorted(dis_sub.items(), key = lambda x: (-x[1], x[0]))) #판매액을 늘리기 위한 할인율 조정
    max_sub = list(dis_sub)[0] #최대 value 가져옴
    # for i in range():

    # print(max_sub)
    


    

            




    # print(users)

    return answer
solution(
[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
solution(
[[40, 10000], [25, 10000]], [7000, 9000])