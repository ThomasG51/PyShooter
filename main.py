import pygame
pygame.init()

from game import Game
game = Game()

# Création de la fenetre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/bg.jpg')

# Game loop
running = True
while running:
    # Application des images du jeu
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)

    # Check action du joueur
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    # Refresh écran
    pygame.display.flip()

    # Game events
    for event in pygame.event.get():
        # Event: Fermeture du jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Event: Appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        # Event: Une touche est relachée
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False