def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if  numbers[i]+numbers[j] <  numbers[j] + numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
    
    numbers = ''.join(numbers)
    if int(numbers) == 0:
        numbers = "0"
        
    answer = numbers

    return answer

solution([6, 10, 2])
solution([3, 30, 34, 5, 9])
solution([1,10,100,1000])
solution([5,545])