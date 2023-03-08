import Node as N
from ChessDataBase import *
from ChessReader5 import *
from ChessGame import *
import graphviz
from graphviz import *


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

    def build(self, dataBase, depthOfTree):

        def split_MoveString(movesString):
            list_of_moves = []
            for element in movesString:
                two_moves = element.split()
                list_of_moves.append(two_moves[0])
                list_of_moves.append(two_moves[1])
            return list_of_moves

        def addResultToNode(game, node):
            result = game.Game_GetResult()[1]
            if (result == '1-0'):
                node.Node_SetWhiteWins(node.Node_GetWhiteWins() + 1)
            elif (result == '0-1'):
                node.Node_SetBlackWins(node.Node_GetBlackWins() + 1)
            elif (result == '1/2-1/2'):
                node.Node_SetRemis(node.Node_GetRemis() + 1)

        games = dataBase.DataBase_GetGames()
        for game in games:
            moves = split_MoveString(game.Game_GetMoves())
            addResultToNode(game, self.rootNode)
            parent_node = self.rootNode
            depth = 0
            for move in moves:
                childNode = N.Node(move)
                new_node = parent_node.Node_AddChildren(childNode)
                addResultToNode(game, new_node)
                parent_node = new_node
                depth += 1
                if depth == depthOfTree:
                    break

        return self.rootNode

    def build_tree_openings(self, opening, dataBase, depthOfTree):
        games = dataBase.DataBase_GetGames()
        newDataBase = ChessDataBase.ChessDataBase('newDataBase')
        for game in games:
            if game.Game_GetOpening()[1] == opening:
                newDataBase.DataBase_AddGame(game)
        return self.build(newDataBase, depthOfTree)



    def visualize(self, database, opening, depthOfTree, filename):
        g = graphviz.Digraph('G', filename=filename , graph_attr={'rankdir':'LR'}, strict = True)
        rootNode = self.build_tree_openings(opening, database, depthOfTree)

        def add_node(node):
            if node.Node_GetMove() == 'Root':
                node.Node_SetMove(opening)
            if node.Node_GetPlayer():
                g.node(f'{node.Node_GetMoveNumber()}. {node.Node_GetMove()}', style = 'filled' , fillcolor='white', label = f'{node.Node_GetMoveNumber()}. {node.Node_GetMove()} \n W: {node.Node_GetWhiteWins()} \n B: {node.Node_GetBlackWins()} \n R: {node.Node_GetRemis()}')
            if not node.Node_GetPlayer():
                g.node(f'{node.Node_GetMoveNumber()}. {node.Node_GetMove()}', style = 'filled' , fillcolor='black', fontcolor = 'white', label = f'{node.Node_GetMoveNumber()}. {node.Node_GetMove()} \n W: {node.Node_GetWhiteWins()} \n B: {node.Node_GetBlackWins()} \n R: {node.Node_GetRemis()}')
            for child in node.children:
                add_node(child)

        def add_edges(node):
            for child in node.children:
                g.edge(f'{node.Node_GetMoveNumber()}. {node.Node_GetMove()}', f'{child.Node_GetMoveNumber()}. {child.Node_GetMove()}')
                add_edges(child)
        

        add_node(rootNode)
        add_edges(rootNode)
        g.view()


  
dataBase = createDataBase(
    '/Users/vegardhatleli/Library/Mobile Documents/com~apple~CloudDocs/NTNU/I&IKT Vår 2023/Avanserte verktøy for performace engineering/innlevering2/chessassignment/Stockfish_15_64-bit.commented.[2600].pgn', 'test')

tree = Tree()
opening = "QGD Slav"
depthOfTree = 5
tree.visualize(dataBase, opening, depthOfTree, 'shallowtree_')
