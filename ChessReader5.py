# 1. Imported Modules
# -------------------

import re
from ChessGame import *
from ChessDataBase import *
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

def stringToMoves(moves_string):
    keep_track_of_move = 1
    last_move_1 = ''
    last_move_2 = ''
    last_move_3 = ''
    last_move_4 = ''
    last_move_5 = ''
    move = ''
    moves = []
    for element in moves_string:
        last_move_1 = last_move_2
        last_move_2 = last_move_3
        last_move_3 = last_move_4
        last_move_4 = last_move_5
        last_move_5 = element
        if (last_move_3 == str(keep_track_of_move) and last_move_4 == '.' and last_move_5 == ' '):
            moves.append(move[:-2])
            move = ''
            keep_track_of_move += 1
        elif ((last_move_3 + last_move_4) == str(keep_track_of_move) and last_move_5 == '.'):
            moves.append(move[:-2])
            move = ''
            keep_track_of_move += 1
        elif ((last_move_2 + last_move_3 + last_move_4) == str(keep_track_of_move) and last_move_5 == '.'):
            moves.append(move[:-2])
            move = ''
            keep_track_of_move += 1
        else:
            move = move + element
    return moves

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
                game = ChessGame.ChessGame(metadata, moves_string)
                games.append(game)
                metadata = []
                step = 2
    return games



database = ChessDataBase.ChessDataBase('testdatabase')
games = ImportChessDataBase(
    '/Users/erikwahlstrom/Performance_Engineering/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn')    

pathVegardErik = [
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn',
    '/Users/erikwahlstrom/Performance_Engineering/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn'
]

for game in games:
    ChessDataBase.ChessDataBase.DataBase_AddGame(database, game)


#print(database.DataBase_GetGames())
'''
for element in database.DataBase_GetGames():
    print(element.Game_GetMetaData())'''