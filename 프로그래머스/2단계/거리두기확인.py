# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    def tes(i, y, x, places, test, test_2):  # i -> y  j -> x
        if places[i][y][x] == "P":
            for k in range(len(test)):
                ch_x = x + test[k][0]
                ch_y = y + test[k][1]
                if (ch_x >= 0 and ch_x < 5) and (ch_y >= 0 and ch_y < 5):
                    # print(ch_x, ch_y, places[i][ch_y][ch_x])
                    if places[i][ch_y][ch_x] == "P":
                        print(i, x, y, ch_x, ch_y)

                        return 1
                    if places[i][ch_y][ch_x] == "O":
                        for t in range(len(test_2[k])):
                            ch_x2 = x + test_2[k][t][0]
                            ch_y2 = y + test_2[k][t][1]
                            if (ch_x2 >= 0 and ch_x2 < 5) and (ch_y2 >= 0 and ch_y2 < 5):
                                if (places[i][ch_y2][ch_x2] == "P"):
                                    print(i, x, y, ch_x2, ch_y2)
                                    return 0

        return 1

    answer = []
    test = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    test_2 = [[[1, 1], [2, 0], [1, -1]],
              [[1, 1], [0, 2], [-1, 1]],
              [[-1, 1], [-2, 0], [-1, -1]],
              [[-1, -1], [0, -2], [1, -1]]]
    dic = {}

    for i in range(len(places)):
        value = 0
        for y in range(len(places[i])):  # j는 y좌표
            for x in range(len(places[i][y])):  # s는 x좌표
                value += tes(i, x, y, places, test, test_2)
        if value != 25:
            answer.append(0)
        else:
            answer.append(1)

    return answer
