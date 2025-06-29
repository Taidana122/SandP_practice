class NoSuchStrategyError(): #Ход не является к, н или б
    pass
class WrongNumberOfPlayersError(): #количество игроков больше 2
    pass

def rps_game_winner(game):
    if len(game) != 2:
        print(WrongNumberOfPlayersError())
    
    player1, choose1 = game[0]
    player2, choose2 = game[1]

    choose=('R', 'P', 'S')
    if choose1 not in choose or choose2 not in choose:
        print(NoSuchStrategyError())
    if choose1 == choose2:
        return player1, choose1
    if choose1 == 'R' and choose2 == 'S':
        return player1, choose1
    if choose1 == 'P' and choose2 == 'R':
        return player1, choose1    
    if choose1 == 'S' and choose2 == 'P':
        return player1, choose1

    if choose1 == 'S' and choose2 == 'R':
        return player2, choose2
    if choose1 == 'R' and choose2 == 'P':
        return player2, choose2    
    if choose1 == 'P' and choose2 == 'S':
        return player2, choose2    
    
print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))