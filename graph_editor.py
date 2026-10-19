import tkinter as tk
from node import Node
from edge import Edge

class GraphEditor:

    def __init__(self, window):
        self.window = window
        self.window.title("Graph Editor")
        self.window.geometry("900x600")

        self.nodes = []
        self.edges = []

        self.selected_node = None
        self.drag_mode = None
        self.is_directed = False

        self.canvas = tk.Canvas(self.window, bg="white", width = 850, height = 550)
        self.canvas.grid(row =0, column=0, padx = 20, pady = 20)

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)


    def on_mouse_down(self, event):
        x, y = event.x, event.y

        clicked_node = None
        for node in self.nodes:
            if node.contains_point(x, y):
                clicked_node = node
                break

        if clicked_node:
            self.selected_node = clicked_node
            self.drag_mode = "move_node"
        else:
            self.selected_node = None
            self.drag_mode = None

            new_id = len(self.nodes) + 1
            new_node = Node(new_id, x, y)

            new_node.draw(self.canvas)
            self.nodes.append(new_node)

    def on_mouse_drag(self, event):
        pass

    def on_mouse_up(self, event):
        self.selected_node = None
        self.drag_mode = False