def solution(players, callings):
    answer = {players:i for i, players in enumerate(players)}

    for call in callings:
        idx = answer[call]
        answer[call] -= 1
        answer[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players