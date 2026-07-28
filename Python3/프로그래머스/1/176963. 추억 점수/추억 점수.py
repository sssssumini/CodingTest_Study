def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        miss = 0
        for j in photo[i]:
            if j in name:
                ind = name.index(j)
                miss += yearning[ind]
        answer.append(miss)
    return answer