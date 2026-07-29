# 자료구조 : 문자열
# 알고리즘 : 문자열 처리
# 시간복잡도 : O(N) 
    # count 연산
# 왜 이 방법을 선택했는가?
    # 대소문자를 구별하지 않기 때문에 p, P의 개수를 카운트해서 합산하여 비교
    
# 문제 타임라인 
    # (p,P) (y,Y)의 개수를 구하여 비교

def solution(s):
    count_p = s.count("p") + s.count("P")
    count_y = s.count("y") + s.count("Y")
    
    if count_p == count_y :
        answer = True
    else :
        answer = False

    return answer

# 더 좋은 풀이
# 먼저 lower() 또는 upper()를 사용하면 순회를 한번만 할 수 있음 
''' 
def solution(s):
    s = s.lower()
    return s.count("p") == s.count("y")
'''