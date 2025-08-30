import pygame
import sys

#TODO Change the damage label to depend, use an if statement
#TODO Optional: Change the sprite or the name of the trains to red blue or green to match
#TODO make screen much wider or make train slower/smaller
pygame.init()

# Screen setup
WIDTH, HEIGHT = 2000, 600  # Wide screen for more space
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Train Crash Simulator")

# Colors
GRAY = (80, 80, 80)
TRACK_COLOR = (50, 50, 50)
RAIL_COLOR = (180, 180, 180)
GREEN = (0, 0, 250)
BLACK = (0, 0, 0)

# Load train images
train_a_img = pygame.image.load("train_red.png")
train_b_img = pygame.image.load("train_blue.png")

# Load possible damage sprites
train_a_damaged_light = pygame.image.load("train_red_damaged_light.png")
train_a_damaged_medium = pygame.image.load("train_red_damaged_medium.png")
train_a_damaged_heavy = pygame.image.load("train_red_damaged_heavy.png")

# train_b_damaged_light = pygame.image.load("train_blue_damaged_light.png")
# train_b_damaged_medium = pygame.image.load("train_blue_damaged_medium.png")
# train_b_damaged_heavy = pygame.image.load("train_blue_damaged_heavy.png")
train_b_damaged_light = pygame.image.load("train_blue.png")
train_b_damaged_medium = pygame.image.load("train_blue.png")
train_b_damaged_heavy = pygame.image.load("train_blue.png")


# Resize all sprites
def resize(img):
    return pygame.transform.scale(img, (160, 100))

train_a_img = resize(train_a_img)
train_b_img = resize(train_b_img)

train_a_damaged_light = resize(train_a_damaged_light)
train_a_damaged_medium = resize(train_a_damaged_medium)
train_a_damaged_heavy = resize(train_a_damaged_heavy)

train_b_damaged_light = resize(train_b_damaged_light)
train_b_damaged_medium = resize(train_b_damaged_medium)
train_b_damaged_heavy = resize(train_b_damaged_heavy)

# Create multiple train cars
def create_train(x, y, num_cars, spacing):
    return [pygame.Rect(x + i * spacing, y, 160, 100) for i in range(num_cars)]

train_a_cars = create_train(100, 270, 3, 170)
train_b_cars = create_train(1900, 270, 3, -170)

# Train speeds and acceleration
train_a_velocity = 0
train_b_velocity = 0
train_a_accel = 0.15
train_b_accel = 0.07
#For train A max speed, every "1" is +12kph max speed, uses x coordinates
train_a_max_speed = 8
train_b_max_speed = -6

font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
crashed = False

# Damage level state
impact_force = 0
damage_level = "light"  # "light", "medium", "heavy"

def draw_tracks():
    pygame.draw.rect(screen, TRACK_COLOR, (0, 290, WIDTH, 20))
    for x in range(0, WIDTH, 40):
        pygame.draw.line(screen, RAIL_COLOR, (x, 285), (x, 315), 3)


def draw_speed():
    kph_a = abs(int(train_a_velocity * 0.2 * 60))
    kph_b = abs(int(train_b_velocity * 0.2 * 60))
    speed_text = font.render(f"Red Train: {kph_a} KPH | Blue Train: {kph_b} KPH", True, BLACK)
    screen.blit(speed_text, (730, 50))

def draw_trains():
    # Pick correct sprite based on crash & damage
    if crashed:
        if damage_level == "light":
            a_img = train_a_damaged_light
            b_img = train_b_damaged_light
        elif damage_level == "medium":
            a_img = train_a_damaged_medium
            b_img = train_b_damaged_medium
        else:
            a_img = train_a_damaged_heavy
            b_img = train_b_damaged_heavy
    else:
        a_img = train_a_img
        b_img = train_b_img

    for car in train_a_cars:
        screen.blit(a_img, car)
    for car in train_b_cars:
        screen.blit(b_img, car)

def move_trains():
    global train_a_velocity, train_b_velocity

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        train_a_velocity = min(train_a_velocity + train_a_accel, train_a_max_speed)
    else:
        train_a_velocity *= 0.95

    train_a_velocity = max(train_a_velocity, 0)

    if train_b_velocity > train_b_max_speed:
        train_b_velocity -= train_b_accel

    for car in train_a_cars:
        car.x += train_a_velocity
    for car in train_b_cars:
        car.x += train_b_velocity

def check_crash():
    return train_a_cars[-1].colliderect(train_b_cars[-1])

def decide_damage():
    global impact_force, damage_level

    relative_speed = abs(train_a_velocity - train_b_velocity)
    impact_force = relative_speed

    #if impact_force < 5.5:
    #    damage_level = "light"
    #elif impact_force < 9:
    #    damage_level = "medium"
    #elif impact_force < 13
    #    damage_level = "heavy"
    #else:
    #    damage_level = "obliterated"
    if impact_force < 5.5:
        damage_level = "light"
    elif impact_force < 9:
        damage_level = "medium"
    else:
        damage_level = "heavy"


def draw_crash_info():
    crash_msg = f"💥 Train Crash! Severity: {damage_level.upper()}"
    speed_label = "Impact Force: {:.2f} | Damage: {}".format(impact_force, damage_level)
    #add if statement
    damage_label = "Damaged Part: Front, sides or multiple cars"

    crash_color = (255, 0, 0)
    text_color = BLACK
    offset_y = 150

    crash_text = font.render(crash_msg, True, crash_color)
    stats_text = font.render(speed_label, True, text_color)
    damage_text = font.render(damage_label, True, text_color)

    x1 = WIDTH // 2 - 200
    base_y = HEIGHT // 2 + offset_y

    screen.blit(crash_text, (x1, base_y - 40))
    screen.blit(stats_text, (x1, base_y))
    screen.blit(damage_text, (x1, base_y + 40))

# Main loop
while True:
    screen.fill(GREEN)
    draw_tracks()
    draw_speed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not crashed:
        move_trains()
        if check_crash():
            crashed = True
            decide_damage()

    draw_trains()

    if crashed:
        draw_crash_info()

    pygame.display.flip()
    clock.tick(60)

