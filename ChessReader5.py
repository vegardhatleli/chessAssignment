# 1. Imported Modules
# -------------------

import re
import pandas as pd
import ChessGame
import ChessDataBase
# 2. Main
# -------


def ImportChessDataBase(filePath):
    inputFile = open(filePath, "r")
    games = ReadChessDataBase(inputFile)
    # for i in range(2):
    # print(Game_GetMoves(games[i]))

    inputFile.close()
    return games


def ExportChessDataBaseToPng(database):
    open('chessgames.pgn', 'w').close()
    games = database.DataBase_GetGames()
    f = open('chessgames.pgn', 'a')
    for game in games:
        ExportChessGameToPng(game)
    f.close()


def ExportChessGameToPng(game):
    f = open('chessgames.pgn', 'a')
    metadata = game.Game_GetMetaData()
    moves = game.Game_GetMoves()
    for data in metadata:
        f.write(data[0] + " " + data[1] + '\n')
    movecount = 1
    for move in moves:
        if (movecount % 10 == 0):
            f.write('\n')
        f.write(f'{movecount}.{move} ')
        movecount += 1
    f.write('\n')
    f.write('\n')
    f.close()

    # With if statement instead of regex


def ReadLine(inputFile):
    line = inputFile.readline()
    if line == "":
        return None
    return line.rstrip()


def ReadChessDataBase(inputFile):
    step = 1
    line = ReadLine(inputFile)
    games = []
    metadata = []
    moves_string = ''

    while True:
        if step == 1:  # Read a game
            if line == None:
                break
            else:
                step = 2
        elif step == 2:  # Read meta-data
            if re.match("\[", line):
                match = re.search("\[([a-zA-Z]+)", line)
                if match:
                    key = match.group(1)
                match = re.search(r'"([^"]+)"', line)
                if match:
                    value = match.group(1)
                metadata.append([key, value])
                line = ReadLine(inputFile)
                if line == None:
                    break
            else:
                step = 3
        elif step == 3:  # read moves
            line = ReadLine(inputFile)
            moves_string = moves_string + str(line)
            if line == None:
                break
            elif re.match("\[([a-zA-Z]+)", line):
                cleaned_string = re.sub(r'\{[^}]*\}', '', moves_string)
                result = re.split(r'\d+\.', cleaned_string)
                result = result[1:]
                substring_to_remove = '[Event "CCRL 40/15"]'
                result[-1] = result[-1].replace(substring_to_remove, '')
                game = ChessGame.ChessGame(metadata, result)
                games.append(game)
                metadata = []
                moves_string = ''
                step = 2
    return games


def createDataBase(inputfile, name):
    games = ImportChessDataBase(inputfile)
    database = ChessDataBase.ChessDataBase(name)
    for game in games:
        ChessDataBase.ChessDataBase.DataBase_AddGame(database, game)
    return database


name = 'testdatabase'
inputfile = '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn'


database = createDataBase(inputfile, name)

pathVegardErik = [
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn',
    '/Users/erikwahlstrom/Performance_Engineering/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn'
]

