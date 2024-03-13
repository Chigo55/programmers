def solution(id_list, report, k):
    answer = []
    dic1 = {name:[] for name in id_list}
    dic2 = {name:0 for name in id_list}
    for i in report:
        val, key = i.split(' ')

        if key in dic1:
            dic1[key].append(val)
        
    for key, val in dic1.items():
        if len(set(val)) >= k:
            for j in set(val):
                dic2[j] += 1

    answer = list(dic2.values())
    return answer