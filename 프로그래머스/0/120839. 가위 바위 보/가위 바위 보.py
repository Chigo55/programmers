def solution(rsp):
    win = {'0':'5', '2':'0', '5':'2'}
    return ''.join([win[h] for h in rsp ])