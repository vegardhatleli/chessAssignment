# Chess Games
class ChessGame:
    def __init__(self, metadata, moves):
        self.metadata = metadata
        self.moves = moves


    def Game_GetMetaData(self):
        return self.metadata


    def Game_SetMetaData(self, event):
        self.metadata = event


    def Game_GetMoves(self):
        return self.moves


    def Game_SetMoves(self, moves):
        self.moves = moves