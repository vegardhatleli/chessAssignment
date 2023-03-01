import pandas as pd
import ChessGame
import ChessDataBase
import ChessReader5


def ExportChessGameToExcel(game, sheet_name):
    metadata = game.Game_GetMetaData()
    moves = game.Game_GetMoves()
    df = pd.DataFrame(metadata, columns=["Key", "Value"])
    df2 = pd.DataFrame(moves, columns=['Moves'])
    writer = pd.ExcelWriter('chessgame.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name,
                header='Metadata', index=False)
    df2.to_excel(writer, sheet_name=sheet_name,
                 index=False, header='Moves', startcol=2, startrow=0)
    writer.save()


# Does not work at the moment, the sheets overwrite themselfs
def ExportChessDataBaseToExcel(database):
    counter = 1
    for game in database:
        ExportChessGameToExcel(game, str(counter))
        counter += 1


def ImportChessGameFromExcel(filepath):
    open_file = pd.read_excel(filepath, sheet_name=0)
    keys = list(open_file['Key'])
    values = list(open_file['Value'])
    moves = list(open_file['Moves'])
    metadata = []
    for i in range(12):
        metadata.append([keys[i], values[i]])
    newGame = ChessGame.ChessGame(metadata, moves)
    return newGame


games = ChessReader5.ImportChessDataBase(
    '/Users/erikwahlstrom/Performance_Engineering/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn'
)
testgame = games[0]

ExportChessGameToExcel(testgame, '1')
# ExportChessDataBaseToExcel(games)
test = ImportChessGameFromExcel('chessgame.xlsx')

print(test.Game_GetOpening())
