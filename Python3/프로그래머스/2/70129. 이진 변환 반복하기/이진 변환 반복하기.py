# 자료구조 :
# 알고리즘 :
# 시간복잡도 :
# 왜 이 방법을 선택했는가?

def solution(s):
    zero_count = 0 # 제거한 0의 개수 
    count = 0
     
    # 추가 아이디어? 
    # 이진법을 어떻게 바꿀 것인가
    while s != "1":
        #s_str = list(s) # split은 공백을 기준으로 나눔
        zero_count += s.count("0")
        new_s = s.replace("0","")
        # if s_str.count("0") > 0 :
        #     for i in range(s_str.count("0")):
        #         s_str.remove("0")
        s = bin(len(new_s))[2:] #이진수로 변환

        count += 1
    # s가 1이 될때까지 
    # 0의 개수를 반환해서 answer에 더해줌
    # 0을 제거하여 s로 반환

    answer = [count, zero_count]
    return answer