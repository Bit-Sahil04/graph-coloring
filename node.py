from config import colors


class Node:
    def __init__(self, x, y, ind):
        self.x = x
        self.y = y
        self.index = ind
        self.pos = (self.x, self.y)
        self.num = None
        self.blocked_colors = []
        self.paths = []
        self.color = 'null'
        self.repulsion = 5
        self.clicked = False

    def assign_color(self):
        for c in colors:
            if c not in self.blocked_colors:
                self.color = c
                self.block_color()
                break

        if self.color == 'null':
            self.color = 'OOB'

    def block_color(self):
        for n in self.paths:
            n.blocked_colors.append(self.color)
