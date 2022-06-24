def solution(lottos, win_nums):
    same = 0
    zero = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            same += 1    
        if lottos[i] == 0:
            zero += 1

    best = 7 - (same + zero)
    worst = 7 - same
    if best > 5:
        best = 6
    if worst > 5:
        worst = 6
    answer = [best, worst]
    return answer











solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19] )
solution([0, 0, 0, 0, 0, 0], 	[38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9]	, 	[20, 9, 3, 45, 4, 35])