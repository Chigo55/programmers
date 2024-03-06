def solution(s):
    zeros = 0
    cnt = 0
    
    while len(s) != 1:
        zeros = zeros + s.count('0')
        s = s.replace('0', '')

        length = len(s)
        s = format(length, 'b')
        cnt += 1
        
    return [cnt, zeros]