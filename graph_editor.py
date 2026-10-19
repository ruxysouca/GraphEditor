import tkinter as tk
from tkinter import messagebox
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

        self.original_x = 0
        self.original_y = 0

        self.canvas = tk.Canvas(self.window, bg="white", width = 850, height = 550)
        self.canvas.grid(row =0, column=0, padx = 20, pady = 20)

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def redraw_canvas(self):
        self.canvas.delete("all")
        for node in self.nodes:
            node.draw(self.canvas)

    def on_mouse_down(self, event):
        x, y = event.x, event.y

        clicked_node = None
        for node in self.nodes:
            if node.contains_point(x, y):
                clicked_node = node
                break

        if clicked_node is not None:
            self.selected_node = clicked_node
            self.drag_mode = "move_node"

            self.original_x = clicked_node.x
            self.original_y = clicked_node.y

        else:
            self.selected_node = None
            self.drag_mode = None

            new_id = len(self.nodes) + 1
            new_node = Node(new_id, x, y)

            new_node.draw(self.canvas)
            self.nodes.append(new_node)

    def on_mouse_drag(self, event):
        if self.drag_mode == "move_node" and self.selected_node is not None:
            self.selected_node.x = event.x
            self.selected_node.y = event.y
            self.redraw_canvas()

    def on_mouse_up(self, event):
        if self.drag_mode == "move_node" and self.selected_node is not None:
            collision = False
            for node in self.nodes:
                if node != self.selected_node:
                    dist = ((node.x - self.selected_node.x) ** 2 + (node.y - self.selected_node.y) ** 2) ** 0.5
                    if dist < (self.selected_node.radius * 2 + 20):
                        collision = True
                        break

            if collision:
                self.selected_node.x = self.original_x
                self.selected_node.y = self.original_y
                messagebox.showwarning(title="Collision warning",
                                       message="Cannot place a node too close or on top of another node!")
                self.redraw_canvas()

        self.selected_node = None
        self.drag_mode = None