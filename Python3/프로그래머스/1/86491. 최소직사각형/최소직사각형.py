def solution(sizes):
    answer = 0
    width = []
    length = []
    for i in sizes:
        i.sort()
        width.append(i[0])
        length.append(i[1])
    answer = (max(width)*max(length))
    return answer