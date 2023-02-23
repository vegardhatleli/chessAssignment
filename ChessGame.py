# Chess Games


def Game_New(metadata, moves):
    return [metadata, moves]


def Game_GetMetaData(game):
    return game[0]


def Game_SetMetaData(game, event):
    game[0] = event


def Game_GetMoves(game):
    return game[1]


def Game_SetMoves(game, moves):
    game[1] = moves
