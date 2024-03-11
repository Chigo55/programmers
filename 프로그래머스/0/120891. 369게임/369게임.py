def solution(order):
    ans = 0
    order = str(order)

    for num in order:
        if num == '3' or num == '6' or num == '9':
            ans += 1

    return ans