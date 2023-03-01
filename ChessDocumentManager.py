from docx import Document
from docx.shared import Inches
import ChessGame
from ChessReader5 import *
from ChessStatistics import *

def writeGameToDocument(dataBase):
    #VALUES
    won_draw_lost = numberOfGamesWonByStockfish(dataBase)
    won_by_Stoclfish_white = numberOfGamesWonByStockfishWhite(dataBase)
    won_by_Stockfish_black = numberOfGamesWonByStockfishBlack(dataBase)

    document = Document()

    document.add_heading('Chessgame statistics', 0)

    document.add_paragraph('Her kan bæsjvi forklare litt om hvordan oppsettet fungerer og hva vi ønsker å ta for oss ')

    document.add_heading('Trekk, hvit : svart', level=1)

    for move in dataBase.DataBase_GetGames()[0].Game_GetMoves():
        document.add_paragraph(
            move, style='List Bullet'
        )
    
    document.add_paragraph('Table regarding number of games won, lost and remis by stockfish')
    #TABLE
    table = document.add_table(rows=2, cols=3, style="Table Grid")
    heading_row = table.rows[0].cells
    # add headings
    heading_row[0].text = "Won"
    heading_row[1].text = "Lost"
    heading_row[2].text = "Remis"
    # access second row's cells
    data_row = table.rows[1].cells
    data_row[0].text = str(won_draw_lost[0])
    data_row[1].text = str(won_draw_lost[1])
    data_row[2].text = str(won_draw_lost[2])

    document.add_paragraph('Table regarding number of games won by stockfish with white or black')
    table1 = document.add_table(rows=2, cols=2, style="Table Grid")
    heading_row1 = table1.rows[0].cells
    heading_row1[0].text = "Won with white"
    heading_row1[1].text = "Won with black"
    data_row1 = table1.rows[1].cells
    data_row1[0].text = str(won_by_Stoclfish_white)
    data_row1[1].text = str(won_by_Stockfish_black)
    
    
    #TODO fyll inn plot
    document.add_picture('EndMove.png', width=Inches(5.25))
    document.add_picture('GamesStillOngoing.png', width=Inches(5.25))

    document.add_page_break()

    document.save('StatDocument.docx')


database = createDataBase('/Users/erikwahlstrom/Performance_Engineering/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn', 'testfil')
game = database.DataBase_GetGames()[0]
writeGameToDocument(database)
