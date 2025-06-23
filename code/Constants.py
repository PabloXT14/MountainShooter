import pygame

# Window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 0)

# Fonts
FONTS = "PressStart2P, Lucida Sans Typewriter, Arial"

# Menu
MENU_OPTIONS = (
    "NEW GAME (1 PLAYER)",
    "NEW GAME (2 PLAYERS - COOPERATIVE)",
    "NEW GAME (2 PLAYERS - COMPETITIVE)",
    "SCORE",
    "QUIT",
)

# Speeds
ENTITIES_SPEED = {
    "Level1Bg0": 0,
    "Level1Bg1": 1,
    "Level1Bg2": 2,
    "Level1Bg3": 3,
    "Level1Bg4": 4,
    "Level1Bg5": 5,
    "Level1Bg6": 5,
    "Player1": 3,
    "Player2": 3,
    "Enemy1": 3,
    "Enemy2": 2,
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
    "Player1": 300,
    "Player2": 300,
    "Enemy1": 50,
    "Enemy2": 60,
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

ENEMY_SPAWN_TIME = 3000  # milissegundos
ENEMY_SPAWN_PADDING = 30
