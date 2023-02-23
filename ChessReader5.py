# 1. Imported Modules
# -------------------

import re
from ChessGame import *
from ChessDataBase import *

# 2. Main
# -------


def ImportChessDataBase(filePath):
    inputFile = open(filePath, "r")
    games = ReadChessDataBase(inputFile)
    # for i in range(2):
    # print(Game_GetMoves(games[i]))

    inputFile.close()
    return games


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
                #print(key + " " + value)
                metadata.append([key, value])
                line = ReadLine(inputFile)
                if line == None:
                    break
            else:
                step = 3
        elif step == 3:  # read moves
            line = ReadLine(inputFile)
            # print(line)
            # moves.append(line)
            moves_string = moves_string + str(line)
            if line == None:
                break
            elif re.match("\[", line):
                game = Game_New(metadata, moves_string)
                games.append(game)
                metadata = []
                step = 2
    return games


database = DataBase_New('testdatabase')
games = ImportChessDataBase(
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn')

for game in games:
    DataBase_AddGame(database, game)

print(database[1][0])
