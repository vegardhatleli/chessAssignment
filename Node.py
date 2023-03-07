class Node:
    def __init__(self, move):
        self.moveNumber = 0
        self.player = False
        self.children = []
        self.move = move
        self.parent = None

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
    
    ### printer

    def print_tree(self):
        spaces = ' ' * self.Node_GetMoveNumber() * 2 
        prefix = spaces + '|_' if self.parent else ''
        print(prefix + self.move)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_chess_tree():

    node = Node('e4')
    node1 = Node('d4')
    node2 = Node('d5')
    node3 = Node('Cf6')
    node4 = Node('e4')
    node5 = Node('d4')
    node6 = Node('d5')
    node7 = Node('Cf6')
    node8 = Node('e4')
    node9 = Node('d4')
    node10 = Node('d5')
    node11 = Node('Cf6')
    node12 = Node('Cf6')
    node13 = Node('e4')
    node14 = Node('d4')
    node15 = Node('d5')
    node16 = Node('Cf6')
    node.Node_AddChildren(node1)
    node.Node_AddChildren(node2)
    node.Node_AddChildren(node3)

    node1.Node_AddChildren(node4)
    node1.Node_AddChildren(node5)
    node1.Node_AddChildren(node6)
    node1.Node_AddChildren(node7)
    
    node2.Node_AddChildren(node8)
    node2.Node_AddChildren(node9)
    node2.Node_AddChildren(node10)
    node2.Node_AddChildren(node11)

    node3.Node_AddChildren(node12)
    node3.Node_AddChildren(node13)
    node3.Node_AddChildren(node14)
    node3.Node_AddChildren(node15)
    return node

#root = build_chess_tree()
#root.print_tree()