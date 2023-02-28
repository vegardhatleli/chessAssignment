# Data base of chess games

import ChessGame
class ChessDataBase:
    def __init__(self, name):
        self.name = name
        self.games = []


    def DataBase_GetName(self):
        return self.name


    def DataBase_SetName(self, name):
        self.name = name

    def DataBase_GetGames(self):
        return self.games


    def DataBase_AddGame(self, game):
        self.games.append(game)
        #games = DataBase_GetGames(dataBase)
        #games.append(game)
