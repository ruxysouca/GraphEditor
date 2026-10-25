import tkinter as tk
import math
class Edge:

    def __init__(self, node1, node2, is_directed = False):
        self.node1 = node1
        self.node2 = node2
        self.is_directed = is_directed

    def connects(self, node1, node2):
        if self.is_directed:
            return self.node1 == node1 and self.node2 == node2
        else:
            return (self.node1 == node1 and self.node2 == node2) or (self.node2 == node1 and self.node1 == node2)

    def draw(self, canvas, color = "black"):
        x1, y1 = self.node1.x, self.node1.y
        x2, y2 = self.node2.x, self.node2.y

        angle = math.atan2(y2-y1, x2-x1)
        radius = self.node2.radius

        target_x = x2 - radius * math.cos(angle)
        target_y = y2 - radius * math.sin(angle)

        arrow_style = tk.LAST if self.is_directed else None
        canvas.create_line(
            x1, y1, target_x, target_y,
            fill=color, width = 2, arrow = arrow_style,
            activefill = "blue", activewidth = 3
        )


