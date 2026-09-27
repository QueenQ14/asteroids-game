import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    dt = 0.0
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for d_item in drawable:
            d_item.draw(screen)
        for u_item in updatable:
            u_item.update(dt)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
