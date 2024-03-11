def solution(quiz):
    ans = []

    for i in quiz:
        i = i.replace(' ', '')
        formula = i.split('=')
        if eval(formula[0]) == int(formula[-1]):
            ans.append('O')
        else:
            ans.append('X')
        
    return ans