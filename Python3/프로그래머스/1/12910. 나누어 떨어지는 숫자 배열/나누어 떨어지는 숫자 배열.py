# 자료구조 : 리스트 
# 알고리즘 : 정렬
# 시간복잡도 : O(N log N)
    # 보통 append는 O(1)
    # sorted => O(K log K)

# 왜 이 방법을 선택했는가?
    # 배열 순환하면서 해당하는 값만 추가 
    
# 문제 타임라인 

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if len(answer) == 0:
        answer = [-1]
    answer = sorted(answer)
    return answer