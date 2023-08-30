# 23시 9분
# 실3
# https://www.acmicpc.net/problem/24060


arr = [6, 5, 3, 1, 8, 7, 2, 4]



def merge_sort(arr):
    if(len(arr) >= 2):
        mid = len(arr)//2
        pre_arr = merge_sort(arr[:mid])
        post_arr = merge_sort(arr[mid:])
        return merge(pre_arr, post_arr)
    return arr

def merge(pre_arr, post_arr):
    ans = []
    pre_idx = 0
    post_idx = 0
    while len(pre_arr) > pre_idx or len(post_arr) > post_idx:
        if pre_idx < len(pre_arr) and (post_idx >= len(post_arr) or pre_arr[pre_idx] < post_arr[post_idx]):
            ans.append(pre_arr[pre_idx])
            pre_idx += 1
        else:
            ans.append(post_arr[post_idx])
            post_idx += 1
    return ans

print(merge_sort(arr))