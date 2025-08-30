import pygame
from constants import *


class Renderer:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.font = pygame.font.SysFont(None, 40)

    def draw_tracks(self):
        """Draw the railway tracks"""
        pygame.draw.rect(self.screen, TRACK_COLOR, (0, 290, WIDTH, 20))
        for x in range(0, WIDTH, 40):
            pygame.draw.line(self.screen, RAIL_COLOR, (x, 285), (x, 315), 3)

    def draw_speed(self, kph_a, kph_b):
        """Draw the speed display"""
        speed_text = self.font.render(f"Red Train: {kph_a} KPH | Blue Train: {kph_b} KPH", True, BLACK)
        self.screen.blit(speed_text, (730, 50))

    def draw_trains(self, train_system):
        """Draw the trains with appropriate sprites"""
        # Pick correct sprite based on crash & damage
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
        # add if statement
        damage_label = "Damaged Part: Front, sides or multiple cars"

        crash_color = (255, 0, 0)
        text_color = BLACK
        offset_y = 150

        crash_text = self.font.render(crash_msg, True, crash_color)
        stats_text = self.font.render(speed_label, True, text_color)
        damage_text = self.font.render(damage_label, True, text_color)

        x1 = WIDTH // 2 - 200
        base_y = HEIGHT // 2 + offset_y

        self.screen.blit(crash_text, (x1, base_y - 40))
        self.screen.blit(stats_text, (x1, base_y))
        self.screen.blit(damage_text, (x1, base_y + 40))