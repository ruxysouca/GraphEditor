import math

class Node:

    def __init__(self, id, x, y, radius = 20):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius

    def contains_point(self, px, py):
        distance = math.sqrt((self.x - px)**2 + (self.y - py)**2)
        return distance <= self.radius

    def draw(self, canvas, color = "lightblue"):
        r = self.radius
        canvas.create_oval(
            self.x - r, self.y - r,
            self.x + r, self.y + r,
            fill = color, outline = "black", width = 2
        )
        canvas.create_text(
            self.x, self.y,
            text = str(self.id),
            font = ("Courier", 10, "bold")
        )