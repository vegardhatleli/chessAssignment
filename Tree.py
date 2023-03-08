import Node as N
from ChessDataBase import *
from ChessReader5 import *
from ChessGame import *


class Tree:
    def __init__(self):
        #self.Name = name
        self.rootNode = N.Node('Root')
        self.treenodes = []

    def split_MoveString(movesString):
        list_of_moves = []
        for element in movesString:
            two_moves = element.split()
            list_of_moves.append(two_moves[0])
            list_of_moves.append(two_moves[1])
        return list_of_moves

    def build(self, dataBase):

        def split_MoveString(movesString):
            list_of_moves = []
            for element in movesString:
                two_moves = element.split()
                list_of_moves.append(two_moves[0])
                list_of_moves.append(two_moves[1])
            return list_of_moves

        def addResultToNode(game, node):
            result = game.Game_GetResult()[1]
            if result == '1-0':
                node.Node_SetWhiteWins(node.Node_GetWhiteWins() + 1)
            elif result == '0-1':
                node.Node_SetBlackWins(node.Node_GetBlackWins() + 1)
            else:
                node.Node_SetRemis(node.Node_GetRemis() + 1)

        games = dataBase.DataBase_GetGames()
        for game in games:
            parent_node = self.rootNode
            moves = split_MoveString(game.Game_GetMoves())
            for move in moves:
                childNode = N.Node(move)
                new_node = parent_node.Node_AddChildren(childNode)
                addResultToNode(game, new_node)
                parent_node = new_node

        return self.rootNode

    def print_tree(self, rootNode):
        spaces = ' ' * rootNode.Node_GetMoveNumber() * 2
        prefix = spaces + '|_' if rootNode.parent else ''
        print(prefix + rootNode.move)
        if rootNode.children:
            for child in rootNode.children:
                child.print_tree()

    def testfunction(dataBase):
        games = dataBase.DataBase_GetGames()
        for game in games:
            print(game.Game_GetMoves())

    def build_test_tree():

        node = N.Node('e4')
        node1 = N.Node('d4')
        node2 = N.Node('d5')
        node3 = N.Node('Cf6')
        node4 = N.Node('e4')
        node5 = N.Node('d4')
        node6 = N.Node('d5')
        node7 = N.Node('Cf6')
        node8 = N.Node('e4')
        node9 = N.Node('d4')
        node10 = N.Node('d5')
        node11 = N.Node('Cf6')
        node12 = N.Node('Cf6')
        node13 = N.Node('e4')
        node14 = N.Node('d4')
        node15 = N.Node('d5')
        node16 = N.Node('Cf6')
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


def build_tree_openings(opening, dataBase):
    openings = []

    tree = Tree()
    # tree.build(games)
    return tree

# GRAPHWIZ


def build_tree():

    dataBase = createDataBase(
        '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn', 'testfil')
    tree = Tree()
    tree.build(dataBase)
    # tree.print_tree(tree.rootNode)
    print(tree.rootNode.children[1].Node_GetMove())
    print('##')
    for element in tree.rootNode.children[1].Node_GetChildren():
        print(element.Node_GetMove())
    print('##')
    list_of_secondMoves = []
    games = dataBase.DataBase_GetGames()
    for game in games:
        if (str(game.Game_GetMoves()[0].split()[0]) == 'd4'):
            list_of_secondMoves.append(str(game.Game_GetMoves()[0].split()[1]))
    print(set(list_of_secondMoves))

    # tree.print_tree(tree.rootNode)


# build_tree()

dataBase = createDataBase(
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn', 'testfil')
tree = Tree()
tree.build(dataBase)

print(tree.rootNode.Node_GetChildren()[0].Node_GetRemis())
