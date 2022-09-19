import pygame, asyncio
from src.settings import *
from src.support import Button, drawText
from src.debug import debug

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(('pygbag' + ' ' + TITLE).title())

async def main():
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill('cyan')
        pygame.display.update()
        await asyncio.sleep(0)

if __name__ == '__main__':
    asyncio.run(main())