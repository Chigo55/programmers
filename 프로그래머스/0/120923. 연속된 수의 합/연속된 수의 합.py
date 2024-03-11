def solution(num, total):
    ans = []
    div = total // num
    flag = False
    cnt = 0
    
    while len(ans) < num:
        if flag:
            total -= (div + cnt)
            ans.append(div + cnt)
            flag = not flag

        else:
            total -= (div - cnt)
            ans.append(div - cnt)
            flag = not flag
            cnt += 1

            
    ans = list(set(ans))
    ans.sort()
            
    return ans