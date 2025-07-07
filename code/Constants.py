import os

import pygame


# Window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

COLOR_RED = (239, 68, 68)

# Fonts
FONTS = os.path.join("assets", "fonts", "PressStart2P-Regular.ttf")

# Menu
MENU_OPTIONS = (
    "NEW GAME (1 PLAYER)",
    "NEW GAME (2 PLAYERS - COOPERATIVE)",
    "NEW GAME (2 PLAYERS - COMPETITIVE)",
    "SCORE",
    "QUIT",
)

# Levels

LEVELS = [
    {
        "name": "Level1",
        "level_number": 1,
        "bg_images_amount": 7,
    },
    {
        "name": "Level2",
        "level_number": 2,
        "bg_images_amount": 5,
    },
    {
        "name": "Level3",
        "level_number": 3,
        "bg_images_amount": 3,
    },
]

# Speeds
ENTITIES_SPEED = {
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Level1Bg4": 4,
    "Level1Bg5": 5,
    "Level1Bg6": 5,
    "Level2Bg0": 0,
    "Level2Bg1": 1,
    "Level2Bg2": 2,
    "Level2Bg3": 4,
    "Level2Bg4": 4,
    "Level3Bg0": 0,
    "Level3Bg1": 1,
    "Level3Bg2": 2,
    "Player1": 3,
    "Player2": 3,
    "Enemy1": 3,
    "Enemy2": 2,
    "Enemy3": 3,
    "Player1Shot": 4,
    "Player2Shot": 4,
    "Enemy1Shot": 8,  # Deve ser maior que a velocidade do inimigo relativamente (para a balada ser mais rápida que o inimigo que está atirando)
    "Enemy2Shot": 7,
    "Enemy3Shot": 10,
}

# Heaths

ENTITY_HEALTH = {
    "Level1Bg0": 999,
    "Level1Bg1": 999,
    "Level1Bg2": 999,
    "Level1Bg3": 999,
    "Level1Bg4": 999,
    "Level1Bg5": 999,
    "Level1Bg6": 999,
    "Level2Bg0": 999,
    "Level2Bg1": 999,
    "Level2Bg2": 999,
    "Level2Bg3": 999,
    "Level2Bg4": 999,
    "Level3Bg0": 999,
    "Level3Bg1": 999,
    "Level3Bg2": 999,
    "Player1": 100,
    "Player2": 100,
    "Enemy1": 50,
    "Enemy2": 60,
    "Enemy3": 50,
    "Player1Shot": 1,
    "Player2Shot": 1,
    "Enemy1Shot": 1,
    "Enemy2Shot": 1,
    "Enemy3Shot": 1,
}

# Damage

ENTITY_DAMAGE = {
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level1Bg5": 0,
    "Level1Bg6": 0,
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    "Level3Bg0": 0,
    "Level3Bg1": 0,
    "Level3Bg2": 0,
    "Player1": 1,
    "Player2": 1,
    "Enemy1": 1,
    "Enemy2": 1,
    "Enemy3": 1,
    "Player1Shot": 20,
    "Player2Shot": 20,
    "Enemy1Shot": 20,
    "Enemy2Shot": 30,
    "Enemy3Shot": 20,
}

# Score (given when entity dies)

ENTITY_SCORE = {
    "Level1Bg0": 0,
    "Level1Bg1": 0,
    "Level1Bg2": 0,
    "Level1Bg3": 0,
    "Level1Bg4": 0,
    "Level1Bg5": 0,
    "Level1Bg6": 0,
    "Level2Bg0": 0,
    "Level2Bg1": 0,
    "Level2Bg2": 0,
    "Level2Bg3": 0,
    "Level2Bg4": 0,
    "Level3Bg0": 0,
    "Level3Bg1": 0,
    "Level3Bg2": 0,
    "Player1": 0,
    "Player2": 0,
    "Enemy1": 100,
    "Enemy2": 125,
    "Enemy3": 150,
    "Player1Shot": 0,
    "Player2Shot": 0,
    "Enemy1Shot": 0,
    "Enemy2Shot": 0,
    "Enemy3Shot": 0,
}

# Players Keys
PLAYER_KEY_UP = {"Player1": pygame.K_UP, "Player2": pygame.K_w}

PLAYER_KEY_DOWN = {"Player1": pygame.K_DOWN, "Player2": pygame.K_s}

PLAYER_KEY_LEFT = {"Player1": pygame.K_LEFT, "Player2": pygame.K_a}

PLAYER_KEY_RIGHT = {"Player1": pygame.K_RIGHT, "Player2": pygame.K_d}

PLAYER_KEY_SHOOT = {"Player1": pygame.K_RCTRL, "Player2": pygame.K_LCTRL}

# Events

EVENT_ENEMY = (
    pygame.USEREVENT + 1
)  # USEREVENT -> constante do pygame geração de eventos, +1 para evitar conflito de eventos

ENEMY_SPAWN_TIME = 2000  # milissegundos
ENEMY_SPAWN_PADDING = 50

TIMEOUT_LIMIT = 20000  # milissegundos
EVENT_TIMEOUT = (
    pygame.USEREVENT + 2
)  # USEREVENT -> constante do pygame geração de eventos, +2 para evitar conflito de eventos
TIMEOUT_DECREMENT_STEP = 100  # milissegundos

# Shots Delay (in milissegundos)
ENTITY_SHOT_DELAY = {
    "Player1": 20,
    "Player2": 15,
    "Enemy1": 50,
    "Enemy2": 100,
    "Enemy3": 70,
}

# Score Texts Positions
SCORE_TEXT_POSITIONS = {
    "Title": (WINDOW_WIDTH / 2, 50),
    "Score": (WINDOW_WIDTH / 2, 100),
    "EnterName": (WINDOW_WIDTH / 2, 140),
    "Name": (WINDOW_WIDTH / 2, 180),
    "Rank": (WINDOW_WIDTH / 2, 100),
    # 0: (WINDOW_WIDTH / 2, 110),
    # 1: (WINDOW_WIDTH / 2, 130),
    # 2: (WINDOW_WIDTH / 2, 150),
    # 3: (WINDOW_WIDTH / 2, 170),
    # 4: (WINDOW_WIDTH / 2, 190),
    # 5: (WINDOW_WIDTH / 2, 210),
    # 6: (WINDOW_WIDTH / 2, 230),
    # 7: (WINDOW_WIDTH / 2, 250),
    # 8: (WINDOW_WIDTH / 2, 270),
    # 9: (WINDOW_WIDTH / 2, 290),
}
