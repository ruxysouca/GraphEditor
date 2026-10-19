import tkinter as tk
from node import Node

class GraphEditor:

    def __init__(self, window):
        self.window = window
        self.window.title("Graph Editor")
        self.window.geometry("900x600")

        self.nodes = []

        self.canvas = tk.Canvas(self.window, bg="white", width = 850, height = 550)
        self.canvas.grid(row =0, column=0, padx = 20, pady = 20)

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        x, y = event.x, event.y

        new_id = len(self.nodes) + 1
        new_node = Node(new_id, x, y)

        new_node.draw(self.canvas)
        self.nodes.append(new_node)
    