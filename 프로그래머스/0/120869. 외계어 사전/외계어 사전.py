def solution(spell, dic):
    for i in dic:
        print(list(set(spell)), list(set(i)))
        if len(i) == len(spell) and set(spell) == set(i):
            return 1
    return 2
            