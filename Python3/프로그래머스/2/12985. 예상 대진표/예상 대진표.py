def solution(n, a, b):
    answer = 0

    if a <= b:
        while True:
            print(a, b, answer)
            if (b % 2 == 0) & (b == (a + 1)):
                answer += 1
                break
            else:
                if a % 2 == 0:
                    a = a // 2
                else:
                    a = a // 2 + 1
                if b % 2 == 0:
                    b = b // 2
                else:
                    b = b // 2 + 1
                answer += 1

    else:
        while True:
            print(a, b, answer)
            if (a % 2 == 0) & (a == (b + 1)):
                answer += 1
                break
            else:
                if a % 2 == 0:
                    a = a // 2
                else:
                    a = a // 2 + 1
                if b % 2 == 0:
                    b = b // 2
                else:
                    b = b // 2 + 1
                answer += 1
    return answer
