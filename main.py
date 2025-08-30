import pygame
import sys
from constants import *
from assets import load_train_assets
from train import TrainSystem
from renderer import Renderer


# TODO Change the damage label to depend, use an if statement
# TODO Optional: Change the sprite or the name of the trains to red blue or green to match
# TODO make screen much wider or make train slower/smaller

def main():
    pygame.init()

    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Train Crash Simulator")

    # Load assets
    assets = load_train_assets()

    # Initialize game systems
    train_system = TrainSystem()
    renderer = Renderer(screen, assets)
    clock = pygame.time.Clock()

    # Main loop
    while True:
        screen.fill(GREEN)
        renderer.draw_tracks()

        # Get speeds for display
        kph_a, kph_b = train_system.get_speeds_kph()
        renderer.draw_speed(kph_a, kph_b)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not train_system.crashed:
            train_system.move_trains()
            if train_system.check_crash():
                train_system.crashed = True
                train_system.decide_damage()

        renderer.draw_trains(train_system)

        if train_system.crashed:
            renderer.draw_crash_info(train_system)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()