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

    def Game_GetEvent(self):
        return self.metadata[0]

    def Game_GetSite(self):
        return self.metadata[1]

    def Game_GetDate(self):
        return self.metadata[2]

    def Game_GetRound(self):
        return self.metadata[3]

    def Game_GetWhite(self):
        return self.metadata[4]

    def Game_GetBlack(self):
        return self.metadata[5]

    def Game_GetResult(self):
        return self.metadata[6]

    def Game_GetECO(self):
        return self.metadata[7]

    def Game_GetOpening(self):
        return self.metadata[8]

    def Game_GetPlyCount(self):
        return self.metadata[9]

    def Game_GetWhiteELO(self):
        return self.metadata[10]

    def Game_GetBlacELO(self):
        return self.metadata[11]

    def Game_GetNthMove(self, n):
        return self.Game_GetMoves()[n]
