# 1. Imported Modules
# -------------------

import re

# 2. Main
# -------


def ImportChessDataBase(filePath):
    inputFile = open(filePath, "r")
    count = ReadChessDataBase(inputFile)
    inputFile.close()


def ReadLine(inputFile):
    line = inputFile.readline()
    if line == "":
        return None
    return line.rstrip()


def ReadChessDataBase(inputFile):
    step = 1
    line = ReadLine(inputFile)
    moves = []
    metadata = []
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
                print(key + " " + value)
                metadata.append((key + " " + value))
                line = ReadLine(inputFile)
                if line == None:

                    break
            else:
                step = 3
        elif step == 3:  # read moves
            line = ReadLine(inputFile)
            moves.append(line)
            if line == None:
                break
            elif re.match("\[", line):
                step = 2
    return metadata, moves


ImportChessDataBase(
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn')
