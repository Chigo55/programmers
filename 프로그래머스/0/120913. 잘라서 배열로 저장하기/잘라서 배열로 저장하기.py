def solution(my_str, n):
    ans = []
    sep = ""
    my_str = list(my_str)

    for i in my_str:
        sep = sep + i
        
        if len(sep) == n:
            ans.append(sep)
            sep = ""

    if len(sep) > 0:
        ans.append(sep)

    return ans