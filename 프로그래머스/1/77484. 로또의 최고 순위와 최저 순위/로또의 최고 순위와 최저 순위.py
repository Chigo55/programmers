def solution(lottos, win_nums):
    high_rank = 0
    low_rank = 0

    for num in lottos:
        if num == 0:
            high_rank += 1
        elif num in win_nums:
            high_rank += 1
            low_rank += 1

    high_rank = 7 - high_rank
    low_rank = 7 - low_rank

    if high_rank >= 6:
        high_rank = 6
    if low_rank >= 6:
        low_rank = 6
        
    return [high_rank, low_rank] 