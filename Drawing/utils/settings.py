import pygame

pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (64,64,64)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 28

PIXEL_SIZE = WIDTH // COLS

TOOLBAR_HEIGHT = HEIGHT-WIDTH

BG_COLOR = BLACK

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size=12)