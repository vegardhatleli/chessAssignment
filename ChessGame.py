# Chess Games


def Game_New(event, opening, metadata, moves):
    return [event, opening, metadata, moves]


def Game_GetEvent(game):
    return game[0]


def Game_SetEvent(game, event):
    game[0] = event


def Game_GetOpening(game):
    return game[1]


def Game_SetOpening(game, opening):
    game[1] = opening


def Game_GetMetaData(game):
    return game[2]


def Game_SetMetaData(game, metadata):
    game[2] = metadata


def Game_GetMoves(game):
    return game[3]


def Game_Moves(game, moves):
    game[3] = moves
