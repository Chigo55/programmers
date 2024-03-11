def solution(array):
    ans = 0
    array = list(map(str, array))

    for nums in array:
        for num in nums:
            if num == '7':
                ans += 1

    return ans