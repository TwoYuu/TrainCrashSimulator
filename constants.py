# constants.py
# Game constants and configuration

# Screen setup
WIDTH, HEIGHT = 2000, 600  # Wide screen for more space

# Colors
GRAY = (80, 80, 80)
TRACK_COLOR = (50, 50, 50)
RAIL_COLOR = (180, 180, 180)
GREEN = (0, 0, 250)
BLACK = (0, 0, 0)
CRASH_COLOR = (255, 0, 0)

# Train physics
TRAIN_A_ACCEL = 0.15
TRAIN_B_ACCEL = 0.07
TRAIN_A_MAX_SPEED = 8  # Every "1" is +12kph max speed
TRAIN_B_MAX_SPEED = -6

# Train dimensions and positioning
TRAIN_WIDTH, TRAIN_HEIGHT = 160, 100
TRAIN_SPACING = 170
TRAIN_A_START_X = 100
TRAIN_B_START_X = 1900
TRAIN_Y = 270
NUM_CARS = 3

# Damage thresholds
LIGHT_DAMAGE_THRESHOLD = 5.5
MEDIUM_DAMAGE_THRESHOLD = 9

# Display settings
FPS = 60
FONT_SIZE = 40
SPEED_DISPLAY_POS = (730, 50)

# Track drawing
TRACK_HEIGHT = 20
RAIL_START_Y = 285
RAIL_END_Y = 315
RAIL_WIDTH = 3
RAIL_SPACING = 40

# Crash display offsets
CRASH_OFFSET_Y = 150
CRASH_X_OFFSET = 200
CRASH_Y_STEP = 40
