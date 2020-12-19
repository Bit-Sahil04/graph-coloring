import math
from config import *


def light_tts(text, x, y, surf, size=10, color=(255, 255, 255)):
    text = str(text)
    font = pygame.font.SysFont('Arial', size, True)

    text_width, text_height = font.size(text)
    text = font.render(text, True, color)
    tRect = surf.blit(text, (x - (text_width / 2), y - (text_height / 2)))
    return tRect


def show_colors(nodes, surf):
    regionX = res[0] * 0.85
    regionY = res[1] * 0.1
    light_tts("Colours", 55 + regionX, regionY, surf, size=30, color=(0, 0, 0))
    pygame.draw.line(surf, (0, 0, 0), (regionX, -10), (regionX, res[1]), 2)
    for i, n in enumerate(nodes):
        pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(regionX + 5, 30 + regionY + i*20, 15, 15))
        light_tts(f"{n.index}", 12 + regionX, 37 + regionY + i * 20, surf, size=15, color=(255, 255, 255))

        for c in range(1, len(colors) - 1):
            mx = 25 + regionX + (c - 1) * 18
            my = 30 + regionY + i * 20
            pygame.draw.rect(surf, colors[c], pygame.Rect(mx, my, 15, 15))
            if c == n.color:
                pygame.draw.rect(surf, (0, 0, 0), pygame.Rect(mx, my, 15, 15), 3)
            if c in n.blocked_colors:
                pygame.draw.line(surf, (0, 0, 0), (mx - 1, my - 1), (mx + 17, my + 17), 3)


def fix_spacing(nodelist):
    for node in nodelist:
        for node2 in nodelist:
            dx = node2.x - node.x
            dy = node2.y - node.y
            dist = 1 + math.sqrt(dx * dx + dy * dy)
            forceX = dx / dist
            forceY = dy / dist

            if node is not node2 and dist < (node_radius + 70):
                node.x -= int(node.repulsion * (forceX * 0.3))
                node.y -= int(node.repulsion * (forceY * 0.3))
        node.pos = (node.x, node.y)
