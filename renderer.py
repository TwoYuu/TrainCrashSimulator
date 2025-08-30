# renderer.py
import pygame
from constants import *


class Renderer:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.font = pygame.font.SysFont(None, FONT_SIZE)

    def draw_tracks(self):
        """Draw the railway tracks"""
        pygame.draw.rect(self.screen, TRACK_COLOR, (0, RAIL_START_Y, WIDTH, TRACK_HEIGHT))
        for x in range(0, WIDTH, RAIL_SPACING):
            pygame.draw.line(self.screen, RAIL_COLOR, (x, RAIL_START_Y), (x, RAIL_END_Y), RAIL_WIDTH)

    def draw_speed(self, kph_a, kph_b):
        """Draw the speed display"""
        speed_text = self.font.render(f"Red Train: {kph_a} KPH | Blue Train: {kph_b} KPH", True, BLACK)
        self.screen.blit(speed_text, SPEED_DISPLAY_POS)

    def draw_trains(self, train_system):
        """Draw the trains with appropriate sprites"""
        if train_system.crashed:
            if train_system.damage_level == "light":
                a_img = self.assets['train_a_damaged_light']
                b_img = self.assets['train_b_damaged_light']
            elif train_system.damage_level == "medium":
                a_img = self.assets['train_a_damaged_medium']
                b_img = self.assets['train_b_damaged_medium']
            else:
                a_img = self.assets['train_a_damaged_heavy']
                b_img = self.assets['train_b_damaged_heavy']
        else:
            a_img = self.assets['train_a']
            b_img = self.assets['train_b']

        for car in train_system.train_a_cars:
            self.screen.blit(a_img, car)
        for car in train_system.train_b_cars:
            self.screen.blit(b_img, car)

    def draw_crash_info(self, train_system):
        """Draw crash information display"""
        crash_msg = f"💥 Train Crash! Severity: {train_system.damage_level.upper()}"
        speed_label = "Impact Force: {:.2f} | Damage: {}".format(train_system.impact_force, train_system.damage_level)
        damage_label = "Damaged Part: Front, sides or multiple cars"

        crash_text = self.font.render(crash_msg, True, CRASH_COLOR)
        stats_text = self.font.render(speed_label, True, BLACK)
        damage_text = self.font.render(damage_label, True, BLACK)

        x1 = WIDTH // 2 - CRASH_X_OFFSET
        base_y = HEIGHT // 2 + CRASH_OFFSET_Y

        self.screen.blit(crash_text, (x1, base_y - CRASH_Y_STEP))
        self.screen.blit(stats_text, (x1, base_y))
        self.screen.blit(damage_text, (x1, base_y + CRASH_Y_STEP))
