food_times = [3, 2, 1]

k = 5


# def solution(food_times, k):
#     arr = []
#     while True:
#         for i in range(len(food_times)):
#             if food_times[i] != 0:
#                 food_times[i] -= 1
#                 arr.append(i)
#         if sum(food_times) <= 0:
#             break
#     return arr[k]+1

def solution(food_times, k):
    arr = []
    while True:
        for i in range(len(food_times)):
            if food_times[i] != 0:
                food_times[i] -= 1
                arr.append(i)
        if sum(food_times) <= 0:
            break
    if len(arr) <= k:
        return -1
    else:
        return arr[k]+1


print(solution(food_times, k))
