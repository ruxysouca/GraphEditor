import tkinter as tk

class Edge:

    def __init__(self, node1, node2, is_directed = False):
        self.node1 = node1
        self.node2 = node2
        self.is_directed = is_directed

    def connects(self, node1, node2):
        return (self.node1 == node1 and self.node2 == node2) or (self.node1 == node2 and self.node2 == node1)

    def draw(self, canvas, color = "black"):
        x1, y1 = self.node1.x, self.node1.y
        x2, y2 = self.node2.x, self.node2.y

        arrow_style = tk.LAST if self.is_directed else tk.NONE
        canvas.create_line(
            x1, y1, x2, y2,
            fill=color, width = 2, arrow = arrow_style,
            activefill = "blue", activewidth = 3
        )


