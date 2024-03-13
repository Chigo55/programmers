def solution(nums):
    return len(list(set(nums))[0:int(len(nums)/2)])