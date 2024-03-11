def solution(i, j ,k):
    ans = 0
    k = str(k)

    for nums in range(i, j+1):
        nums = str(nums)

        for num in nums:
            if k == num:
                ans += 1

    return ans