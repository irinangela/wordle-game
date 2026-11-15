import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():      # 1. handle events
        if event.type == pygame.QUIT:
            running = False

    screen.fill((18, 18, 19))             # 3. draw
    pygame.display.flip()
    clock.tick(60)

pygame.quit()