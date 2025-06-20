from ui import start_menu, show_end_menu, promotion_menu, draw_board, draw_pieces, draw_dots, draw_back_button
from logic import ChessLogic
import bot
import pygame
import chess
import sys

pygame.init()

WIDTH, HEIGHT = 640, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

SQUARE_SIZE = WIDTH // 8
BOARD_Y_OFFSET = 60
logic = ChessLogic()

def main():
    while True:
        mode_info = start_menu(WIN, WIDTH)
        if isinstance(mode_info, tuple):
            mode, difficulty = mode_info
        else:
            mode = mode_info
            difficulty = "easy"

        logic.reset_board()
        selected = None
        legal_moves = []
        run = True

        while run:
            WIN.fill((0, 0, 0))
            draw_board(WIN, WIDTH, BOARD_Y_OFFSET)
            draw_pieces(WIN, logic.board, SQUARE_SIZE, BOARD_Y_OFFSET)
            draw_dots(WIN, legal_moves, SQUARE_SIZE, BOARD_Y_OFFSET)
            back_rect = draw_back_button(WIN, WIDTH)

            pygame.display.flip()

            if logic.board.turn == chess.BLACK and mode == "vs_bot":
                pygame.time.wait(500)
                move = bot.get_bot_move(logic.board, difficulty)
                logic.push_move(move)
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        run = False
                        break

                    square = logic.get_square(pygame.mouse.get_pos(), SQUARE_SIZE, BOARD_Y_OFFSET)
                    if selected is None:
                        if logic.board.piece_at(square) and logic.board.piece_at(square).color == logic.board.turn:
                            selected = square
                            legal_moves = logic.get_legal_moves(selected)
                    else:
                        if logic.is_promotion(selected, square):
                            promo_choice = promotion_menu(WIN, WIDTH)
                            move = chess.Move(selected, square, promotion=chess.Piece.from_symbol(promo_choice).piece_type)
                        else:
                            move = chess.Move(selected, square)

                        logic.push_move(move)
                        selected = None
                        legal_moves = []

            status, winner = logic.get_game_status()
            if status == "checkmate":
                result = show_end_menu(WIN, WIDTH, f"Checkmate! {winner} wins")
                if result == "restart":
                    break
                elif result == "menu":
                    return
            elif status == "stalemate":
                result = show_end_menu(WIN, WIDTH, "Stalemate!")
                if result == "restart":
                    break
                elif result == "menu":
                    return

if __name__ == "__main__":
    main()
