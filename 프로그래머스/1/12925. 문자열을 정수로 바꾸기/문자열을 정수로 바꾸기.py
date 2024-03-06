def solution(s):
    if s[0] == "-":
        s = int(s[1:])
        s = -s
    else:
        s = int(s)
    return s