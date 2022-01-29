import os
import random
import sys

import pygame

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bombs(pygame.sprite.Sprite):
    bomb = 'bomb.png'
    boom = 'boom.png'

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(Bombs.bomb)
        self.boom_b = pygame.transform.scale(load_image(Bombs.boom), (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(25, width - 100)
        self.rect.y = random.randrange(25, height - 100)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.boom_b
            self.rect.x -= 25
            self.rect.y -= 25


all_sprites = pygame.sprite.Group()

size = width, height = 500, 500

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
running = True

for _ in range(20):
    Bombs()

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        for el in all_sprites:
            el.update(event)

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)