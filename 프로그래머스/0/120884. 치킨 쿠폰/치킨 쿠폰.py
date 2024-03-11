def solution(chicken):
    ans = 0
    quo, rem = divmod(chicken, 10)
    ans += quo

    while quo + rem >= 10:
        quo, rem = divmod(quo + rem, 10)
        ans += quo
        
    return ans