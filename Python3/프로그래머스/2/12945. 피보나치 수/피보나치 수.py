def solution(n):
    a = 0 
    b = 1 
    f = a+b # F(2)
    for i in range(n-2) :
        fibo = b+f
        a,b,f = b, f, fibo
    answer = f%1234567
    return answer