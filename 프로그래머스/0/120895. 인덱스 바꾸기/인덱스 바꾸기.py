def solution(my_string, num1, num2):
    answer = []
    words = [[idx, word] for idx, word in enumerate(my_string)]
    for idx, string in words:
        print(idx)
        if idx == num1:
            idx = num2
            answer.append([idx, string])
        elif idx == num2:
            idx = num1
            answer.append([idx, string])
        else:
            answer.append([idx, string])

    answer.sort(key = lambda x: x[0])
    answer = list(zip(*answer))
    answer = ''.join(answer[-1])
    return answer