def solution(n):
    answer = 0
    
    div = 10 
    while n > 0 :
        answer += (n%div)
        n //= div

    return answer