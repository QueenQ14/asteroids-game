import pygame
from constants import *
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    dt = 0.0
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield1 = AsteroidField()


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
            for a_item in asteroids:
                for s_item in shots:
                    if a_item.collides_with(s_item):
                        log_event("asteroid_shot")
                        a_item.split()
                        s_item.kill()
                if a_item.collides_with(player1):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
                
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
