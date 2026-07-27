def solution(s):
    num = s.split() # 구분자 sep 
    b, s = int(num[0]), int(num[0])
    for i in range(1, len(num)):
        if b < int(num[i]) : b = int(num[i])
        if s > int(num[i]) : s = int(num[i])
    
    answer = str(s) + " " + str(b)
    return answer