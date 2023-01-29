# [제약사항]

# 1.     점의 개수 N은 1 이상 300 이하이다. (1 ≤ N ≤ 300)

# 2.     점들과 시작점의 좌표는 1 이상 5,000 이하이다.

# 3.     점들, 혹은 점과 시작점이 겹치는 경우는 없다.
#설계방식
#1. 시작 점의 위치가 어디있는지 확인한다.
#2. 시작점의 위치가 최소점 보다 왼쪽에 있으면 쭉 오른쪽으로 이동
#3. 시작점의 위치가 최대점 보다 오른쪽에 있으면 쭉 왼쪽으로 이동
#4. 시작점이 최소,  최대 사이에 있으면 절대값(최소 - 현재)*2 +  (최대 - 현재)
# 
#input 예시 1. testcase 갯수    int
#           2. node 개수    int
#           3. 현재 시작 위치 int
#           4. 노드의 위치(list)
import math
def main():
    testCount = int(input())
    
    for i in range(testCount):
        nodeCount, start = map(int, input().split())
        nodes = sorted([int(num) for num in input().split()])
        printAnswer(i+1, solution(start, nodes))
def solution(start, nodes):
    maxvalue = max(nodes)
    minvalue = min(nodes)
    max_dif = abs(max(nodes)- start)
    min_dif = abs(min(nodes) - start)
    if start < minvalue:
        return max(nodes) - start
    if start > maxvalue:
        return start - minvalue
    if(max_dif > min_dif):
        return min_dif * 2 + max_dif
    else:
        return max_dif * 2 + min_dif

    
def printAnswer(testCount, answer):
    print('#%d'% testCount,answer)


if __name__ == "__main__":
    main()

# 1 3 4  