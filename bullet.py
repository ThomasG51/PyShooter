import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.velocity = 8
        self.player = player
        self.rect.x = player.rect.x + (player.rect.width / 1.5)
        self.rect.y = player.rect.y + (player.rect.height / 2.5)
        self.origin_image = self.image
        self.angle = 0


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        if self.rect.x > 1080:
            self.remove()

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.bullets.remove(self)