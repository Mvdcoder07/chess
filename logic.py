import chess

class ChessLogic:
    def __init__(self):
        self.board = chess.Board()

    def reset_board(self):
        self.board.reset()

    def get_square(self, pos, square_size, offset):
        x, y = pos
        col = x // square_size
        row = 7 - ((y - offset) // square_size)
        return chess.square(col, row)

    def get_legal_moves(self, square):
        return [m for m in self.board.legal_moves if m.from_square == square]

    def is_promotion(self, from_square, to_square):
        return (
            self.board.piece_type_at(from_square) == chess.PAWN and
            (chess.square_rank(to_square) == 0 or chess.square_rank(to_square) == 7)
        )

    def push_move(self, move):
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False

    def get_game_status(self):
        if self.board.is_checkmate():
            return "checkmate", "White" if self.board.turn == chess.BLACK else "Black"
        elif self.board.is_stalemate():
            return "stalemate", None
        elif self.board.is_check():
            return "check", None
        return None, None
