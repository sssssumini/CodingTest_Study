def solution(a, b):
    day = "SUN,MON,TUE,WED,THU,FRI,SAT"
    date = day.split(",")
    d = b
    for i in range(1,a):
        if (i==1 or i==3 or i==5 or i ==7 or i==8 or i == 10 or i==12):
            d += 31
        elif (i==2):
            d += 29
        else: d+=30
    
    return (date[(d+4)%7])