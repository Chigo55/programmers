def solution(participant, completion):
    import collections
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]