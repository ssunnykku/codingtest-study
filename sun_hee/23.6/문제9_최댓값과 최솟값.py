def solution(s):
    array = [int(i) for i in s.split(" ")]
    array_max = str(max(array))
    array_min = str(min(array))

    return (" ").join([array_min, array_max])
