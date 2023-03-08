class Node:
    def __init__(self, move):
        self.moveNumber = 0
        self.player = False
        self.children = []
        self.move = move
        self.parent = None
        self.white_wins = 0
        self.black_wins = 0
        self.remis = 0

    def Node_GetMoveNumber(self):
        return self.moveNumber

    def Node_GetMove(self):
        return self.move

    def Node_GetPlayer(self):
        return self.player

    def Node_GetChildren(self):
        return self.children

    def Node_GetParent(self):
        return self.parent

    def Node_SetMoveNumber(self, newMoveNumber):
        self.moveNumber = newMoveNumber

    def Node_SetMove(self, newMove):
        self.move = newMove

    def Node_SetPlayer(self, newPlayer):
        self.player = newPlayer

    def Node_AddChildren(self, child):
        for element in self.children:
            if (element.Node_GetMove() == child.Node_GetMove()):
                return element
        else:
            child.Node_SetMoveNumber(self.Node_GetMoveNumber() + 1)
            child.Node_SetPlayer(not self.Node_GetPlayer())
            child.Node_SetParent(self)
            self.children.append(child)
            return child

    def Node_SetParent(self, newParent):
        self.parent = newParent

    def Node_GetWhiteWins(self):
        return self.white_wins

    def Node_GetBlackWins(self):
        return self.black_wins

    def Node_GetRemis(self):
        return self.remis

    def Node_SetWhiteWins(self, newWins):
        self.white_wins = newWins

    def Node_SetBlackWins(self, newWins):
        self.black_wins = newWins

    def Node_SetRemis(self, newRemis):
        self.remis = newRemis

    # printer

    def print_tree(self):
        spaces = ' ' * self.Node_GetMoveNumber() * 2
        prefix = spaces + '|_' if self.parent else ''
        print(prefix + self.move)
        if self.children:
            for child in self.children:
                child.print_tree()
