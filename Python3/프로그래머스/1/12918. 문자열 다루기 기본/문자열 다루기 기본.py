def solution(s):
    num = ["0","1","2","3","4","5","6","7","8","9"]
    for i in (s) :
        print(i)
        if i not in num:
            answer = False
            break
        else: 
            answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    return answer