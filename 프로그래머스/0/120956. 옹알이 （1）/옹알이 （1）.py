def solution(babbling):
    answer = 0

    for i in babbling:
        words = ['aya', 'ye', 'woo', 'ma']
        for j in range(len(words)):
            word = words.pop(0)
            i = i.replace(word, ' ')

            if not i.strip():
                answer += 1
                break
    return answer