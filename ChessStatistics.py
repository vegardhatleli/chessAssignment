from ChessReader5 import *
import ChessGame
import ChessDataBase
import ChessReader5
import numpy as np
import matplotlib.pyplot as plt
import math


def NumberOfGamesWon(chessDatabase):
    count = [0, 0, 0]
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
    count = [0, 0, 0]  # W - L - D
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


def plotLastMoveBarChart_Total(database):
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


def plotGamesStillOnGoing_Total(database):
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
    plt.savefig("GamesStillOnGoingTotal.png")
    plt.show()


def plotGamesStillOnGoing_StockFish(database):
    games = database.DataBase_GetGames()
    whitegames = []
    blackgames = []
    total = np.zeros(215)
    for game in games:
        endmove = len(game.Game_GetMoves())
        total[endmove] = total[endmove] + 1

    white = np.zeros(215)
    black = np.zeros(215)
    for game in games:
        if str(game.Game_GetWhite()[1][0:9]) == 'Stockfish':
            whitegames.append(game)
        else:
            blackgames.append(game)
    ###
    totalplot = np.full(215, 2600)
    pregames = 0
    for i in range(215):
        totalplot[i] = totalplot[i] - total[i] - pregames
        pregames += total[i]

    for game in whitegames:
        endmove = len(game.Game_GetMoves())
        white[endmove] = white[endmove] + 1
    for game in blackgames:
        endmove = len(game.Game_GetMoves())
        black[endmove] = black[endmove] + 1

    x = np.arange(215)
    whiteplots = np.full(215, len(whitegames))
    blackplots = np.full(215, len(blackgames))
    pregames = 0
    for i in range(215):
        whiteplots[i] = whiteplots[i] - white[i] - pregames
        pregames += white[i]
    pregames = 0
    for i in range(215):
        blackplots[i] = blackplots[i] - black[i] - pregames
        pregames += black[i]

    plt.xlabel("Moves")
    plt.ylabel("Games")
    plt.title("How many games ongoing after N'th move")
    plt.plot(x, whiteplots, color='r', label='Stockfish white')
    plt.plot(x, blackplots, color='b', label='Stockfish black')
    plt.plot(x, totalplot, color='g', label='Total')
    plt.legend()
    plt.savefig("GamesStillOngoingStockfish.png")
    plt.show()


def CalculateMeanValueOfMoves_Total(database):
    games = database.DataBase_GetGames()
    endmoves = []
    for game in games:
        endmoves.append(len(game.Game_GetMoves()))
    return round(sum(endmoves)/len(endmoves), 3)


def CalculateStandardDeviation_Total(database):
    games = database.DataBase_GetGames()
    endmoves = []
    for game in games:
        endmoves.append(len(game.Game_GetMoves()))
    n = len(endmoves)
    if n < 2:
        return 0
    mean = sum(endmoves) / n
    variance = sum((x - mean)**2 for x in endmoves) / (n - 1)
    return round(math.sqrt(variance), 3)


def CalculateMeanValueOfMoves_StockfishWhite(database):
    games = database.DataBase_GetGames()
    whitegames = []
    for game in games:
        if str(game.Game_GetWhite()[1][0:9]) == 'Stockfish':
            whitegames.append(game)
    endmoves = []
    for game in whitegames:
        endmoves.append(len(game.Game_GetMoves()))
    return round(sum(endmoves)/len(endmoves), 3)


def CalculateStandardDeviation_StockfishWhite(database):
    games = database.DataBase_GetGames()
    whitegames = []
    for game in games:
        if str(game.Game_GetWhite()[1][0:9]) == 'Stockfish':
            whitegames.append(game)
    endmoves = []
    for game in whitegames:
        endmoves.append(len(game.Game_GetMoves()))
    n = len(endmoves)
    if n < 2:
        return 0
    mean = sum(endmoves) / n
    variance = sum((x - mean)**2 for x in endmoves) / (n - 1)
    return round(math.sqrt(variance), 3)


def CalculateMeanValueOfMoves_StockfishBlack(database):
    games = database.DataBase_GetGames()
    blackgames = []
    for game in games:
        if str(game.Game_GetWhite()[1][0:9]) != 'Stockfish':
            blackgames.append(game)
    endmoves = []
    for game in blackgames:
        endmoves.append(len(game.Game_GetMoves()))
    return round(sum(endmoves)/len(endmoves), 3)


def CalculateStandardDeviation_StockfishBlack(database):
    games = database.DataBase_GetGames()
    blackgames = []
    for game in games:
        if str(game.Game_GetWhite()[1][0:9]) != 'Stockfish':
            blackgames.append(game)
    endmoves = []
    for game in blackgames:
        endmoves.append(len(game.Game_GetMoves()))
    n = len(endmoves)
    if n < 2:
        return 0
    mean = sum(endmoves) / n
    variance = sum((x - mean)**2 for x in endmoves) / (n - 1)
    return round(math.sqrt(variance), 3)


def plotGamesStillOnGoing_StockfishWonOrLost(database):
    games = database.DataBase_GetGames()
    wongames = []
    lostgames = []
    won = np.zeros(215)
    lost = np.zeros(215)
    for game in games:
        if (str(game.Game_GetWhite()[1][0:9]) == 'Stockfish' and game.Game_GetResult()[1] == '1-0') or ((str(game.Game_GetWhite()[1][0:9])) != 'Stockfish' and game.Game_GetResult()[1] == '0-1'):
            wongames.append(game)
        elif (str(game.Game_GetWhite()[1][0:9]) == 'Stockfish' and game.Game_GetResult()[1] == '0-1') or ((str(game.Game_GetWhite()[1][0:9])) != 'Stockfish' and game.Game_GetResult()[1] == '1-0'):
            lostgames.append(game)
    ###
    print(len(wongames))
    print(len(lostgames))
    for game in wongames:
        endmove = len(game.Game_GetMoves())
        won[endmove] = won[endmove] + 1
    for game in lostgames:
        endmove = len(game.Game_GetMoves())
        lost[endmove] = lost[endmove] + 1

    x = np.arange(215)
    wonplots = np.full(215, len(wongames))
    lostplots = np.full(215, len(lostgames))
    pregames = 0
    for i in range(215):
        wonplots[i] = wonplots[i] - won[i] - pregames
        pregames += won[i]
    pregames = 0
    for i in range(215):
        lostplots[i] = lostplots[i] - lost[i] - pregames
        pregames += lost[i]

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].plot(x, wonplots, color='r', label='Stockfish won')
    axs[0].set_xlabel("Moves")
    axs[0].set_ylabel("Games")
    axs[0].set_title(
        "How many games ongoing after N't move and won by Stockfish")
    plt.title("How many games ongoing after N'th move")
    axs[1].plot(x, lostplots, color='b', label='Stockfish lost')
    axs[1].set_xlabel("Moves")
    axs[1].set_ylabel("Games")
    axs[1].set_title(
        "How many games ongoing after N't move and lost by Stockfish")
    plt.legend()
    plt.savefig("GamesStillOngoingStockfishWonorLost.png")
    plt.show()

# CALCULTE MATH HERE THAN DONE


def CalculateMeanValueOfMoves_StockfishWon(database):
    games = database.DataBase_GetGames()
    wongames = []
    for game in games:
        if (str(game.Game_GetWhite()[1][0:9]) == 'Stockfish' and game.Game_GetResult()[1] == '1-0') or ((str(game.Game_GetWhite()[1][0:9])) != 'Stockfish' and game.Game_GetResult()[1] == '0-1'):
            wongames.append(game)
    endmoves = []
    for game in wongames:
        endmoves.append(len(game.Game_GetMoves()))
    return round(sum(endmoves)/len(endmoves), 3)


def CalculateStandardDeviation_StockfishWon(database):
    games = database.DataBase_GetGames()
    wongames = []
    for game in games:
        if (str(game.Game_GetWhite()[1][0:9]) == 'Stockfish' and game.Game_GetResult()[1] == '1-0') or ((str(game.Game_GetWhite()[1][0:9])) != 'Stockfish' and game.Game_GetResult()[1] == '0-1'):
            wongames.append(game)
    endmoves = []
    for game in wongames:
        endmoves.append(len(game.Game_GetMoves()))
    n = len(endmoves)
    if n < 2:
        return 0
    mean = sum(endmoves) / n
    variance = sum((x - mean)**2 for x in endmoves) / (n - 1)
    return round(math.sqrt(variance), 3)


def CalculateMeanValueOfMoves_StockfishLost(database):
    games = database.DataBase_GetGames()
    lostgames = []
    for game in games:
        if (str(game.Game_GetWhite()[1][0:9]) == 'Stockfish' and game.Game_GetResult()[1] == '0-1') or ((str(game.Game_GetWhite()[1][0:9])) != 'Stockfish' and game.Game_GetResult()[1] == '1-0'):
            lostgames.append(game)
    endmoves = []
    for game in lostgames:
        endmoves.append(len(game.Game_GetMoves()))
    return round(sum(endmoves)/len(endmoves), 3)


def CalculateStandardDeviation_StockfishLost(database):
    games = database.DataBase_GetGames()
    lostgames = []
    for game in games:
        if (str(game.Game_GetWhite()[1][0:9]) == 'Stockfish' and game.Game_GetResult()[1] == '0-1') or ((str(game.Game_GetWhite()[1][0:9])) != 'Stockfish' and game.Game_GetResult()[1] == '1-0'):
            lostgames.append(game)
    endmoves = []
    for game in lostgames:
        endmoves.append(len(game.Game_GetMoves()))
    n = len(endmoves)
    if n < 2:
        return 0
    mean = sum(endmoves) / n
    variance = sum((x - mean)**2 for x in endmoves) / (n - 1)
    return round(math.sqrt(variance), 3)


def ExtractOpeningResults(database):
    games = database.DataBase_GetGames()
    opening_results = {}
    for game in games:
        opening = game.Game_GetOpening()[1]
        result = game.Game_GetResult()[1]
        if (opening not in opening_results.keys()):
            opening_results[opening] = [0, 0, 0]
        if result == '1-0':
            opening_results[opening][0] += 1
        elif result == '0-1':
            opening_results[opening][1] += 1
        else:
            opening_results[opening][2] += 1
    return opening_results


def ExtractOpeningResultsofGamesPlayedNTimes(database, n):
    opening_results = ExtractOpeningResults(database)
    new_opening_results = {}
    for opening in opening_results:
        times_played = opening_results[opening][0] + \
            opening_results[opening][1] + opening_results[opening][2]
        if times_played >= n:
            new_opening_results[opening] = [opening_results[opening][0],
                                            opening_results[opening][1], opening_results[opening][2]]
    return new_opening_results


# database = createDataBase('/Users/erikwahlstrom/Performance_Engineering/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn', 'testdatabase')


database = createDataBase(
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn', 'testdatabase')


# plotGamesStillOnGoing_StockFish(database)

#dick = ExtractOpeningResults(database)

#plotGamesStillOnGoing_StockfishWonOrLost(database)
dick = ExtractOpeningResultsofGamesPlayedNTimes(database, 10)

print(dick)
