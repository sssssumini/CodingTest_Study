def solution(phone_book):
    answer = True
    # 아이디어 : 정렬 먼저 하면 인접한것만 확인해도 됨
    phone = sorted(phone_book)
    for i in range(len(phone)-1) :
        if (phone[i+1].startswith(phone[i])) == True:
            answer = False
            break
    return answer