import pygame, asyncio
from src.settings import *
from src.support import Button, drawText
from src.debug import debug

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(TITLE)

def main():
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        display.fill('cyan')

        surf = pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(surf, (0, 0))

        pygame.display.update()

if __name__ == '__main__':
        main()
