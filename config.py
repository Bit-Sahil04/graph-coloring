import pygame

#  High number of colors are not visible on-screen at lower window resolution
colors = {
    1: (255, 0, 0),
    2: (0, 255, 0),
    3: (200, 20, 128),
    4: (127, 127, 127),
    5: (152, 53, 91),
    6: (44, 200, 100),
    7: (100, 44, 200),
    'null': (0, 0, 0),  # Default Color
    'OOB': (180, 200, 10),  # Color to denote that the node is "Out of bounds" or cannot be colored.
}

pygame.init()
res = (1024, 768)
screen = pygame.display.set_mode(res)
node_radius = 15
boundaryX = 150
boundaryY = 50
