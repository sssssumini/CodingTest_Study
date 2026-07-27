def solution(n):
    num = list(str(n))
    num_sort = sorted(num, reverse = 0)
    answer = 0
    
    for i in range(len(num_sort)):
        answer += (10**i)*int(num_sort[i])
    
    return answer