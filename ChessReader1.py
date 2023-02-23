import re

# This reader prints the amount of games played


def ImportChessDataBase(filePath):
    inputFile = open(filePath, "r")
    count = ReadChessDataBase(inputFile)
    inputFile.close()
    return count


def ReadChessDataBase(inputFile):
    count = 0
    for line in inputFile:
        line = line.rstrip()  # remove the end of the line character
        if re.search("Event", line):
            count = count + 1
    return count


count = ImportChessDataBase(
    "/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/Chess/Stockfish_15_64-bit.commented.[2600].pgn")
print(count)
