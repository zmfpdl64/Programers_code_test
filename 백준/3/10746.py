#18시 25분 #19시 34분
# 0.5초 512MB 1<=  n <= 15   0<=r     c <= 2^n

#해결 방법: 전체에서 4사분면으로 쪼개면서 값을 더하는 방식으로 계산했다.
#1사분면이라면 현재 조사하고 있는 4사분면의 0/4 2사분면이라면 1/4 이런식으로 더하면서 배열의 크기가 1이 될때까지 재귀함수를 실행했다.
#시간이 오래걸린 이유: 2사분면을 계산할때 max_col/2로 계산해야하는데 max_col로 그냥 실행하여 정상적으로 동작하지 않았다...


n, y, x= map(int, input().split())

sum = 0
def div_map(max_col, max_row):
    if max_col == 1 or max_row == 1:
        return 
    global x, y, sum
    cur_row = max_row/2
    cur_col = max_col/2
    mul = 0
    if x < cur_col and y < cur_row:        #1사분면
        pass
    elif x >= cur_col and y < cur_row:       #2사분면
        x = x - cur_col
        mul = 1/4
    elif x < cur_col and y >= cur_row:     #3사분면
        y = y - cur_row
        mul = 2/4
    else:
        x = x - cur_col
        y = y - cur_row
        mul = 3/4
    sum += mul * (max_col*max_row)
    div_map(max_col/2, max_row/2)
div_map(2**n, 2**n)
print(int(sum))