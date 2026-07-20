def solution(s):
    answer = True
    
    check = 0
    s = list(s)

    if s[0] == ")" :
        answer = False 
    else:
        for i in range(len(s)):
            if s[i] == "(": 
                check+=1
            else: 
                check-=1
            if check < 0: 
                break
        if check != 0:
            answer = False
        else: 
            answer = True

    
    return answer