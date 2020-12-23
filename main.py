import sys
import random

from config import *
from node import *
from utilities import light_tts, fix_spacing, show_colors


def get_paths(listnodes):
    for n1 in listnodes:
        for n2 in listnodes:
            if random.randint(0, 1) == 0 or (n1 is n2) or (n1 in n2.paths):
                continue
            else:
                n1.paths.append(n2)
                n2.paths.append(n1)


def generate_nodes(num):
    nodes = []
    for i in range(num + 1):
        x = random.randint(0 + (boundaryX - 50), res[0] - boundaryX)
        y = random.randint(0 + boundaryY, res[1] - boundaryY)
        n = Node(x, y, i)
        n.num = i
        nodes.append(n)

    return nodes


def main():
    max_nodes = 4
    fps = 60
    pygame.display.set_caption("Greedy Graph Coloring - Bit-Sahil04")
    clock = pygame.time.Clock()
    left = False
    right = False
    down = False
    up = False
    lmb = False
    nodelist = generate_nodes(max_nodes)
    get_paths(nodelist)
    curr_node = 0
    mx, my = [0, 0]
    while True:
        screen.fill((255, 255, 255))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == pygame.BUTTON_LEFT:
                    lmb = True
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == pygame.BUTTON_LEFT:
                    lmb = False
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    left = True
                elif e.key == pygame.K_RIGHT:
                    right = True
                    max_nodes += 1
                elif e.key == pygame.K_UP:
                    up = True
                    max_nodes -= 1
                elif e.key == pygame.K_DOWN:
                    down = True

        show_colors(nodelist, screen)
        fix_spacing(nodelist)
        mx, my = pygame.mouse.get_pos()

        for node in nodelist:
            for path in node.paths:
                pygame.draw.line(screen, (0, 0, 0), node.pos, path.pos)

        for node in nodelist:
            br = pygame.draw.circle(screen, colors[node.color], node.pos, node_radius)
            light_tts(f"{node.index}", node.x, node.y, screen, size=15, color=(255, 255, 255))

            if br.collidepoint(mx, my) and lmb:
                node.clicked = True
            if node.clicked and not lmb:
                node.clicked = False

            if node.clicked:
                node.x = mx
                node.y = my

        if down:
            del nodelist
            curr_node = 0
            nodelist = generate_nodes(max_nodes)
            get_paths(nodelist)

        if left:
            nodelist[curr_node].assign_color()
            if curr_node < max_nodes:
                curr_node += 1

        left = False
        right = False
        up = False
        down = False
        clock.tick(fps)
        pygame.display.flip()


if __name__ == '__main__':
    main()
