def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(completion)):
        print(participant[i], completion[i])    #길이가 하나 적은 completion길이만큼 반복하여 비교하여
        if participant[i] != completion[i]:     #answer에 paticipant값을 저장한다.
            answer = participant[i]
            break
    if answer == '':
        answer = participant[-1]    #만약 answer에 값이 없다면 particiapnt의 마지막 값을 넣어준다.

    return answer

solution( ["leo", "kiki", "eden", ],["eden", "kiki"])

solution( ["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])

solution( ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
