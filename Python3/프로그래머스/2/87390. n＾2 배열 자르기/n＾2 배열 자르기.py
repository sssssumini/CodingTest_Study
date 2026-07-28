def solution(n, left, right):
    answer = []
    # result =  [[0] * n for _ in range(n)] # n행 n열의 값이 전부 0인 2차원 리스트 생성 
    # for i in range(n) :
    #     for j in range(n) :
    #         m = max(i,j)
    #         result[i][j] = (m+1)
    # for i in range(left, right+1) :
    #     answer.append(result[i//n][i%n])
                
    for i in range(left, right+1) :
        m = max(i//n+1,i%n+1)
        answer.append(m)

    return answer