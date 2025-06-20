# ui.py
import pygame
import sys

def start_menu(win, width):
    font_title = pygame.font.SysFont(None, 60)
    font_option = pygame.font.SysFont(None, 40)

    title = font_title.render("Chess Game", True, (255, 255, 255))
    opt1 = font_option.render("1 vs 1", True, (255, 255, 255))
    opt2 = font_option.render("vs Bot", True, (255, 255, 255))

    rect1 = opt1.get_rect(center=(width // 2, 300))
    rect2 = opt2.get_rect(center=(width // 2, 380))
    title_rect = title.get_rect(center=(width // 2, 150))

    while True:
        win.fill((10, 10, 50))
        pygame.draw.rect(win, (70, 130, 180), rect1.inflate(20, 10))
        pygame.draw.rect(win, (70, 130, 180), rect2.inflate(20, 10))
        win.blit(title, title_rect)
        win.blit(opt1, rect1)
        win.blit(opt2, rect2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    return "1v1"
                elif rect2.collidepoint(event.pos):
                    return ("vs_bot", bot_difficulty_menu(win, width))

def bot_difficulty_menu(win, width):
    font = pygame.font.SysFont(None, 40)
    options = [("Easy", "easy"), ("Normal", "normal"), ("Hard", "hard")]
    rects = []

    while True:
        win.fill((20, 20, 60))
        for i, (label, value) in enumerate(options):
            text = font.render(label, True, (255, 255, 255))
            rect = text.get_rect(center=(width // 2, 250 + i * 60))
            pygame.draw.rect(win, (100, 149, 237), rect.inflate(20, 10))
            win.blit(text, rect)
            rects.append((rect, value))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, difficulty in rects:
                    if rect.collidepoint(event.pos):
                        return difficulty

def draw_board(win, width, offset):
    square_size = width // 8
    colors = [(245, 245, 245), (125, 135, 150)]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(win, color, (col * square_size, row * square_size + offset, square_size, square_size))

def draw_pieces(win, board, square_size, offset):
    import os
    pieces = {}
    for piece in ["r", "n", "b", "q", "k", "p"]:
        for color in ["w", "b"]:
            img_path = os.path.join("asset", f"{color}{piece}.svg")
            image = pygame.image.load(img_path)
            pieces[color + piece] = pygame.transform.scale(image, (square_size, square_size))

    for square in board.piece_map():
        piece = board.piece_at(square)
        row = 7 - (square // 8)
        col = square % 8
        piece_str = f"{'w' if piece.color else 'b'}{piece.symbol().lower()}"
        win.blit(pieces[piece_str], (col * square_size, row * square_size + offset))

def draw_dots(win, moves, square_size, offset):
    for move in moves:
        square = move.to_square
        row = 7 - (square // 8)
        col = square % 8
        center = (col * square_size + square_size // 2, row * square_size + offset + square_size // 2)
        pygame.draw.circle(win, (0, 255, 0), center, 10)

def draw_back_button(win, width):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Back", True, (255, 255, 255))
    rect = text.get_rect(topleft=(10, 10))
    pygame.draw.rect(win, (0, 0, 0), rect.inflate(10, 5))
    win.blit(text, rect)
    return rect

def promotion_menu(win, width):
    font = pygame.font.SysFont(None, 36)
    options = ["q", "r", "b", "n"]
    labels = ["Queen", "Rook", "Bishop", "Knight"]
    rects = []

    win.fill((0, 0, 0))
    for i, label in enumerate(labels):
        text = font.render(label, True, (255, 255, 255))
        rect = text.get_rect(center=(width // 2, 100 + i * 60))
        win.blit(text, rect)
        rects.append((rect, options[i]))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, option in rects:
                    if rect.collidepoint(event.pos):
                        return option

def show_end_menu(win, width, message):
    font = pygame.font.SysFont(None, 48)
    button_font = pygame.font.SysFont(None, 36)
    text = font.render(message, True, (255, 255, 255))
    rect = text.get_rect(center=(width // 2, 200))

    restart_text = button_font.render("Restart", True, (255, 255, 255))
    menu_text = button_font.render("Main Menu", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(width // 2, 300))
    menu_rect = menu_text.get_rect(center=(width // 2, 360))

    while True:
        win.fill((0, 0, 0))
        win.blit(text, rect)
        win.blit(restart_text, restart_rect)
        win.blit(menu_text, menu_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    return "restart"
                elif menu_rect.collidepoint(event.pos):
                    return "menu"
