#1. new_id의 첫번째 문단에 숫자가 들어있는가?
#2. 첫번째 문단과 동일한 아이디가 존재하는가 
#3. 두번째 문단에서 숫자가 처음시작 0이 될 순 없다.
#4. 두번째 문단에서 s + n + s 가 될 순 없다.
#5. 

import re

dic = {}

def solution(register_list, new_id):
    answer = ''
    for i in range(len(register_list)):
        register_list[i] = re.split('([^a-z])', register_list[i], maxsplit = 1)
        if len(register_list[i]) >= 2:
            register_list[i][1] = ''.join(register_list[i][1:])
            register_list[i] = register_list[i][:2]
        if ''.join(register_list[i]) not in dic: #필요 여하에 따라 복잡도 줄이기
            dic[''.join(register_list[i])] = True
    new_id_split = re.split('([^a-z])', new_id, maxsplit = 1)
    new_string = new_id_split[0]
    sum_id = ''
    new_number = 1
    if len(new_id_split) > 2:
        new_id_split[1] = ''.join(new_id_split[1:])
        new_id_split = new_id_split[:2]
        new_number = int(new_id_split[1])
        sum_id = ''.join(new_id_split)
    else:
        sum_id = new_id_split[0]
    if sum_id in dic:
        while True:
            id = new_string + str(new_number)
            if id in dic:  #사전에 있을 때
                pass
            else:
                dic[id] = True #사전에 없을 때
                return id
            new_number += 1
    else:
        dic[sum_id] = True
        return sum_id




            
    

    

    print(register_list)

    return answer


# print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
# print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
print(solution(
["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
print(solution(["apple1", "orange", "banana3"], "apple"))