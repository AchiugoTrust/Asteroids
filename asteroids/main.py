import pygame
from constants import *
from player import *

pygame.init()
pygame.time.Clock()
player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


dt = 0




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

    dt = 1000 / pygame.time.Clock.tick(60)


    
    
    



if __name__ == "__main__":
    main()
