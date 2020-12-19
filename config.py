import pygame

colors = {
    1: (255, 0, 0),
    2: (0, 255, 0),
    3: (200, 20, 128),
    4: (127, 127, 127),
    5: (152, 53, 91),
    'null': (0, 0, 0),  # Default Color
    'OOB': (180, 200, 10),  # Color to denote that the node is "Out of bounds" or cannot be colored.
}

pygame.init()
res = (800, 600)
screen = pygame.display.set_mode(res)
node_radius = 10
