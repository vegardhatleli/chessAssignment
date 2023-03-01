from ChessReader5 import *


def NumberOfGamesWon(chessDatabase):
    count = [0,0,0]
    for game in chessDatabase.DataBase_GetGames():
        if len(game.Game_GetResult()[1]) == 7:
            count[2] += 1
        if len(game.Game_GetResult()[1]) == 3:
            if int(game.Game_GetResult()[1][0]) == int(1):
                count[0] += 1
            else:
                count[1] += 1
    return count

def gameIsRemis(game):
    if len(game.Game_GetResult()[1]) == 7:
        return True
    else:
        return False

def gameIsWonByWhite(game):
    if len(game.Game_GetResult()[1]) == 3:
        if int(game.Game_GetResult()[1][0]) == int(1):
            return True
        else:  
            return False

def numberOfGamesWonByStockfish(chessDatabase):
    count = [0,0,0] # W - L - D
    for game in chessDatabase.DataBase_GetGames():
        if str(game.Game_GetWhite()[1][0:9]) == 'Stockfish':
            if gameIsRemis(game):
                count[2] += 1
            elif gameIsWonByWhite(game):
                count[0] += 1
            else:
                count[1] += 1
        else:
            if gameIsRemis(game):
                count[2] += 1
            elif gameIsWonByWhite(game):
                 count[1] += 1
            else:
                count[0] += 1
        
    return count

def numberOfGamesWonByStockfishWhite(chessDatabase):
    count = 0
    for game in chessDatabase.DataBase_GetGames():
        if str(game.Game_GetWhite()[1][0:9]) == 'Stockfish':
            if gameIsWonByWhite(game):
                count += 1
    return count

def numberOfGamesWonByStockfishBlack(chessDatabase):
    count = 0
    for game in chessDatabase.DataBase_GetGames():
        if str(game.Game_GetWhite()[1][0:9]) != 'Stockfish':
            if gameIsRemis(game) == False and gameIsRemis(game) == False:
                count += 1
    return count
    
database = createDataBase('/Users/erikwahlstrom/Performance_Engineering/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn', 'testdatabase')

'''

n = numberOfGamesWonByStockfish(database)
t = numberOfGamesWonByStockfishWhite(database)
o = numberOfGamesWonByStockfishBlack(database)
print(n)
print(t)
print(o)
'''