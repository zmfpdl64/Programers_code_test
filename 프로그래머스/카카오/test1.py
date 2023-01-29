#today 2021.05.12
#terms 'A 6'
#privacies 
# 1<= d <= 28 , 1<= m <= 12
def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int,today.split('.'))
    grade = {i.split()[0]: int(i.split()[1])  for i in terms}
    docs = [[list(map(int,i.split(' ')[0].split('.'))), i.split(' ')[1]] for i in privacies]
    print(docs)
    print(y, m, d)
    print("grade ", grade) #grade 'A' : '6'
    for i in range(len(docs)): # i = [['2021', '05', '02'], 'A']
        y_c = y - docs[i][0][0]
        m_c = m - docs[i][0][1]
        d_c = d - docs[i][0][2]
        # print(y_c, m_c, d_c)
        dline = grade[docs[i][1]] * 28 #기한 >= 남은날
        days = y_c*12*28 + m_c*28 + d_c #남은 날
        # print(days, dline)
        if days >= dline:
            answer.append(i+1)
        


    return answer

# print(int('01'))
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))