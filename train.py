# train_system.py
import pygame
from constants import *


class TrainSystem:
    def __init__(self):
        # Create multiple train cars
        self.train_a_cars = self._create_train(TRAIN_A_START_X, TRAIN_Y, NUM_CARS, TRAIN_SPACING)
        self.train_b_cars = self._create_train(TRAIN_B_START_X, TRAIN_Y, NUM_CARS, -TRAIN_SPACING)

        # Train speeds and acceleration
        self.train_a_velocity = 0
        self.train_b_velocity = 0

        # Crash state
        self.crashed = False
        self.impact_force = 0
        self.damage_level = "light"

    def _create_train(self, x, y, num_cars, spacing):
        """Create multiple train cars"""
        return [pygame.Rect(x + i * spacing, y, TRAIN_WIDTH, TRAIN_HEIGHT) for i in range(num_cars)]

    def move_trains(self):
        """Handle train movement and physics"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.train_a_velocity = min(self.train_a_velocity + TRAIN_A_ACCEL, TRAIN_A_MAX_SPEED)
        else:
            self.train_a_velocity *= 0.95

        self.train_a_velocity = max(self.train_a_velocity, 0)

        if self.train_b_velocity > TRAIN_B_MAX_SPEED:
            self.train_b_velocity -= TRAIN_B_ACCEL

        for car in self.train_a_cars:
            car.x += self.train_a_velocity
        for car in self.train_b_cars:
            car.x += self.train_b_velocity

    def check_crash(self):
        """Check if trains have collided"""
        return self.train_a_cars[-1].colliderect(self.train_b_cars[-1])

    def decide_damage(self):
        """Calculate damage level based on impact force"""
        relative_speed = abs(self.train_a_velocity - self.train_b_velocity)
        self.impact_force = relative_speed

        if self.impact_force < LIGHT_DAMAGE_THRESHOLD:
            self.damage_level = "light"
        elif self.impact_force < MEDIUM_DAMAGE_THRESHOLD:
            self.damage_level = "medium"
        else:
            self.damage_level = "heavy"

    def get_speeds_kph(self):
        """Get train speeds in KPH for display"""
        kph_a = abs(int(self.train_a_velocity * 0.2 * 60))
        kph_b = abs(int(self.train_b_velocity * 0.2 * 60))
        return kph_a, kph_b
