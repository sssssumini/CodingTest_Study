# 자료구조 : 문자열
# 알고리즘 : 시뮬레이션 + 구현
# 시간복잡도 : O(N logN) 
    # while 문 O(logN) 안에서 count(), replace() >> O(N)번 반복
# 왜 이 방법을 선택했는가?
    # 처음 방법 : s를 리스트로 변경하여 리스트 안에서 0의 개수만큼 0을 제거
    # 문제점 : 시간 초과
    # 해결 : 문자열 그대로 replace를 사용하여 시간을 줄임 
    
# 문제 타임라인 
    # s가 1이 될때까지 
    # 0의 개수를 반환해서 answer에 더해줌
    # 0을 제거하여 s로 반환
    
def solution(s):
    zero_count = 0 # 제거한 0의 개수 
    count = 0 # 실행한 횟수 
     
    # 추가 아이디어? 
    # 이진법을 어떻게 바꿀 것인가
    while s != "1":
        #s_str = list(s) # split은 공백을 기준으로 나눔
        zero_count += s.count("0")
        new_s = s.replace("0","")
        # zero_count += len(s) - len(new_s) 
            # count 한번 줄일 수 있음
        
        # if s_str.count("0") > 0 :
        #     for i in range(s_str.count("0")):
        #         s_str.remove("0")
        s = bin(len(new_s))[2:] #이진수로 변환

        count += 1
    
    answer = [count, zero_count]
    return answer