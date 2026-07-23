def solution(phone_number):
    if len(phone_number) > 4 :
        for i in range(len(phone_number)-4) :
            phone_number = phone_number[:i] + "*" + phone_number[i+1:]
    return phone_number
