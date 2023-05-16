# 14시 02분
# 14시 51분

# https://school.programmers.co.kr/learn/courses/30/lessons/17686

# 1. 문자열 분리
# 2. 이름, 숫자, 파일종류
# def custom_sort(lst):
#     def sort_key(x):
#         return (x[0].lower(), int(x[1]), x[3])
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if sort_key(lst[i]) > sort_key(lst[j]):
#                 lst[i], lst[j] = lst[j], lst[i]
#     return lst
# def custom_sort(lst):
#     def quicksort(arr):
#         if len(arr) <= 1:
#             return arr
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if sort_key(x) < sort_key(pivot)]
#         middle = [x for x in arr if sort_key(x) == sort_key(pivot)]
#         right = [x for x in arr if sort_key(x) > sort_key(pivot)]
#
#         return quicksort(left) + middle + quicksort(right)
#     def sort_key(x):
#         return (x[0].lower(), -int(x[1]), x[3])
#     return quicksort(lst)

def custom_sort(lst):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if sort_key(left[i]) <= sort_key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    def sort_key(x):
        return (x[0].lower(), -int(x[1]), x[3])
    return merge_sort(lst)
def my_sort(lists):
    for i in range(len(lists) - 1):
        for j in range(i + 1, len(lists)):
            if ((lists[i][0].lower(), -int(lists[i][1]), lists[i][3]) > (lists[j][0].lower(), -int(lists[j][1]), lists[j][3])):
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def solution(files):
    answer = []
    lists = [[] for _ in range(len(files))]

    for idx, file in enumerate(files):
        for i in range(len(file) - 1):
            if (file[i].isalpha() or not file[i].isalnum()) and (file[i + 1].isalnum() and not file[i + 1].isalpha()):
                lists[idx].append(file[:i + 1])
                for j in range(i + 1, len(file)):
                    if file[j].isalnum():
                        pass
                    else:
                        lists[idx].append(file[i + 1:j])
                        lists[idx].append(file[j:])
                        lists[idx].append(idx)
                        break
                else:
                    lists[idx].append(file[i + 1:])
                    lists[idx].append('')
                    lists[idx].append(idx)

                break
    # lists = my_sort(lists)
    lists = custom_sort(lists)
    # lists.sort(key=lambda x: ((x[0].lower(), -int(x[1]), x[3])))

    for i in lists:
        answer.append(''.join(i[:-1]))
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))