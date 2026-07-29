def solution(a, b, c, d):
    answer = 0
    input_dice = [a, b, c, d]
    dice = []
    for i in range(1, 7):
        dice.append(input_dice.count(i))

    print(dice)

    if max(dice) == 4:
        p = dice.index(4)
        answer = (p + 1) * 1111
    elif max(dice) == 3:
        p = dice.index(3) + 1
        q = dice.index(1) + 1
        answer = (10 * p + q) ** 2
    elif max(dice) == 2:
        if 1 in dice:
            temp = []
            for i in range(len(dice)):
                if dice[i] == 1:
                    temp.append(i + 1)
            answer = temp[0]*temp[1]
        else:
            temp = []
            for i in range(len(dice)):
                if dice[i] == 2:
                    temp.append(i + 1)
            answer = (temp[1] + temp[0]) * (temp[1] - temp[0])

    else:
        answer = dice.index(1) + 1

    return answer