import ChessGame
import ChessDataBase
import ChessReader5
import numpy as np
import matplotlib.pyplot as plt

# Settes inn i Statistic "klassen"


def plotLastMoveBarChart(database):
    games = database.DataBase_GetGames()
    x = np.arange(215)
    y = np.zeros(215)
    for game in games:
        endmove = len(game.Game_GetMoves())
        y[endmove] = y[endmove] + 1

    plt.bar(x, y, color='blue')
    plt.xlabel("Moves")
    plt.ylabel("Games")
    plt.title("How many moves before end of game")
    plt.savefig("EndMove.png")
    plt.show()


def plotGamesStillOnGoing(database):
    games = database.DataBase_GetGames()
    chart = np.zeros(215)
    for game in games:
        endmove = len(game.Game_GetMoves())
        chart[endmove] = chart[endmove] + 1

    x = np.arange(215)
    y = np.full(215, 2600)
    pregames = 0
    for i in range(215):
        y[i] = y[i] - chart[i] - pregames
        pregames += chart[i]

    plt.xlabel("Moves")
    plt.ylabel("Games")
    plt.title("How many games ongoing after N'th move")
    plt.plot(x, y)
    plt.savefig("GamesStillOngoing.png")
    plt.show()


database = ChessDataBase.ChessDataBase('testdatabase')
games = ChessReader5.ImportChessDataBase(
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn')

for game in games:
    ChessDataBase.ChessDataBase.DataBase_AddGame(database, game)

plotLastMoveBarChart(database)
plotGamesStillOnGoing(database)
