import os
import pygame


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Не удалось загрузить изображение!")
        raise SystemExit(message)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 600, 300

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 200
running = True

x, y = -600, 0
img = load_image('gameover.png')

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    if x < 0:
        x += 1

    screen.fill((0, 0, 255))
    screen.blit(img, (int(x), y))

    pygame.display.flip()
    clock.tick(fps)