# solution 1
# del은 비용이 O(n)이 나옴
# def solution(arr):
#     answer = []

#     while True:
#         if len(arr) > 1:
#             if arr[0] == arr[1]:
#                 del arr[0]
#             else:
#                 answer.append(arr[0])
#                 del arr[0]
#         elif len(arr) == 1:
#             answer.append(arr[0])
#             del arr[0]
#         else:
#             break

#     return answer

# 앞뒤 숫자를 비교
def solution(arr):
    answer = []
    for i in range(0,len(arr)):
        if i == 0 :
            answer.append(arr[0])
        else:
            if (arr[i] != arr[i-1]) :
                answer.append(arr[i])
    return answer