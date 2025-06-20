import random
import chess

def get_easy_move(board: chess.Board):
    return random.choice(list(board.legal_moves))

def get_normal_move(board: chess.Board):
    """
    Medium-level bot that evaluates captures and mobility.
    Prioritizes material gain.
    """
    best_score = -float('inf')
    best_move = None

    for move in board.legal_moves:
        board.push(move)
        score = evaluate_board(board)
        board.pop()

        if score > best_score:
            best_score = score
            best_move = move

    return best_move if best_move else get_easy_move(board)

def evaluate_board(board: chess.Board):
    """
    Simple evaluation: material count.
    """
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    value = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            val = piece_values[piece.piece_type]
            value += val if piece.color == board.turn else -val

    return value

def get_hard_move(board: chess.Board):
    return get_easy_move(board)  # placeholder

def get_bot_move(board: chess.Board, difficulty: str = "easy"):
    if difficulty == "easy":
        return get_easy_move(board)
    elif difficulty == "normal":
        return get_normal_move(board)
    elif difficulty == "hard":
        return get_hard_move(board)
    else:
        raise ValueError("Invalid difficulty level")
