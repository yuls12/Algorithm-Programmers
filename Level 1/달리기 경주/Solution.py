def solution(players, callings):
    player = {name: i for i, name in enumerate(players)}

    for name in callings:
        pre, index = player[name] - 1, player[name]
        players[pre], players[index] = players[index], players[pre]
        player[players[pre]], player[players[index]] = player[
            players[pre]] - 1, player[players[index]] + 1

    return players
