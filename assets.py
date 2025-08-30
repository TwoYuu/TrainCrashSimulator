import pygame
from constants import TRAIN_WIDTH, TRAIN_HEIGHT


def load_and_resize_image(path):
    """Load an image and resize it to train dimensions"""
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (TRAIN_WIDTH, TRAIN_HEIGHT))


def load_train_assets():
    """Load all train sprites and return them as a dictionary"""
    assets = {}

    # Load normal train images
    assets['train_a'] = load_and_resize_image("assets/train_red.png")
    assets['train_b'] = load_and_resize_image("assets/train_blue.png")

    # Load damaged train images for train A
    assets['train_a_damaged_light'] = load_and_resize_image("assets/train_red_damaged_light.png")
    assets['train_a_damaged_medium'] = load_and_resize_image("assets/train_red_damaged_medium.png")
    assets['train_a_damaged_heavy'] = load_and_resize_image("assets/train_red_damaged_heavy.png")

    # Load damaged train images for train B (using blue.png as placeholder)
    assets['train_b_damaged_light'] = load_and_resize_image("assets/train_blue.png")
    assets['train_b_damaged_medium'] = load_and_resize_image("assets/train_blue.png")
    assets['train_b_damaged_heavy'] = load_and_resize_image("assets/train_blue.png")

    return assets