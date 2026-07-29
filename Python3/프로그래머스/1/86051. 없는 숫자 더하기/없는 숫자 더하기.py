# 자료구조 : 리스트
# 알고리즘 : 수학
# 시간복잡도 : O(N) 
    # sum 연산 시 리스트 한번 순회함 
# 왜 이 방법을 선택했는가?
    # numbers에 중복이 없다고 명시되어 있어 전체합에서 리스트 sum값을 빼서 반환
# 문제 타임라인 
    # 0-9중 없는 수의 합계를 구하기 
    
def solution(numbers):
    total = (0+9)*10/2 # 0-9 합
    answer = total - sum(numbers)
    
    return answer
