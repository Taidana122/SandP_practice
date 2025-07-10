class NoSuchStrategyError(Exception): #Ход не является к, н или б
    pass
class WrongNumberOfPlayersError(Exception): #количество игроков больше 2
    pass

def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError()
    
    player1, choose1 = game[0]
    player2, choose2 = game[1]

    choose=('R', 'P', 'S')
    if choose1 not in choose or choose2 not in choose:
        raise NoSuchStrategyError()
    if choose1 == choose2:
        return f"{player1} {choose1}"
    if choose1 == 'R' and choose2 == 'S':
        return f"{player1} {choose1}"
    if choose1 == 'P' and choose2 == 'R':
        return f"{player1} {choose1}"   
    if choose1 == 'S' and choose2 == 'P':
        return f"{player1} {choose1}"

    if choose1 == 'S' and choose2 == 'R':
        return f"{player2} {choose2}"
    if choose1 == 'R' and choose2 == 'P':
        return f"{player2} {choose2}"    
    if choose1 == 'P' and choose2 == 'S':
        return f"{player2} {choose2}"
