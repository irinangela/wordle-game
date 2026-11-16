import pygame
from wordle import WordleGame, load_words

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Wordle")
words = load_words('words_english.json')
game = WordleGame(words)
clock = pygame.time.Clock()

MESSAGES = {
    "wrong_length": "Please enter a 5-letter word",
    "not_a_word": "Invalid word. Please try again",
    "duplicate": "You have already guessed that word",
}
message = ""
message_until = 0
small_font = pygame.font.SysFont(None, 32)

TILE = 62 
GAP = 5
ROWS = 6
COLS = 5
COLORS = {
    '🟩': (83, 141, 78),
    '🟨': (181, 159, 59),
    '⬜': (58, 58, 60),
}

font = pygame.font.SysFont(None, 48)

grid_width = COLS * TILE + (COLS - 1) * GAP
grid_height = ROWS * TILE + (ROWS - 1) * GAP

left_margin = (500 - grid_width) // 2
top_margin = (600 - grid_height) // 2

def draw_letter(screen, letter, x, y):
    letter_surface = font.render(letter.upper(), True, (255, 255, 255))
    letter_rect = letter_surface.get_rect(center=(x + TILE // 2, y + TILE // 2))
    screen.blit(letter_surface, letter_rect)

def draw_grid(screen, game, current_input):
    for r in range(ROWS):
        for c in range(COLS):
            x = left_margin + c * (TILE + GAP)
            y = top_margin + r * (TILE + GAP)
            if r < len(game.history):
                guess, feedback = game.history[r]
                pygame.draw.rect(screen, COLORS[feedback[c]], (x, y, TILE, TILE), border_radius=3)
                draw_letter(screen, guess[c], x, y)
            else:
                pygame.draw.rect(screen, COLORS['⬜'], (x, y, TILE, TILE), 2, border_radius=3)
                if r == len(game.history) and c < len(current_input):
                    draw_letter(screen, current_input[c], x, y)
            
current_input = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game.over:
                if event.key == pygame.K_RETURN:
                    game = WordleGame(words)
                    current_input = ""
                    message_until = 0
            else:
                if event.key == pygame.K_BACKSPACE:
                    current_input = current_input[:-1]
                elif event.key == pygame.K_RETURN:
                    result = game.guess(current_input)
                    if result == "ok":
                        current_input = ""
                    elif result in MESSAGES:
                        message = MESSAGES[result]
                        message_until = pygame.time.get_ticks() + 2000
                else:
                    if len(current_input) < COLS and event.unicode.isascii() and event.unicode.isalpha():
                        current_input += event.unicode

    screen.fill((18, 18, 19))
    draw_grid(screen, game, current_input)

    if pygame.time.get_ticks() < message_until:
        surf = small_font.render(message, True, (255, 255, 255))
        screen.blit(surf, surf.get_rect(center=(250, 60)))

    if game.over:
        if game.won:
            text = "Congratulations!"
        else:
            text = f"The word was {game.answer.upper()}"
        surf = small_font.render(text, True, (255, 255, 255))
        screen.blit(surf, surf.get_rect(center=(250, 540)))
        hint = small_font.render("Press Enter to play again", True, (150, 150, 150))
        screen.blit(hint, hint.get_rect(center=(250, 570)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()