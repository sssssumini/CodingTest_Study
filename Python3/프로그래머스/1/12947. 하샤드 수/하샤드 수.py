def solution(x):
    answer = True
    
    num = list(map(int,list(str(x))))
    num_sum = sum(num)
    if x % num_sum == 0 :
        answer = True
    else : 
        answer = False
    
    return answer