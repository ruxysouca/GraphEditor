import tkinter as tk
from tkinter import messagebox
from node import Node
from edge import Edge

class GraphEditor:

    def __init__(self, window):
        self.window = window
        self.window.title("Graph Editor")
        self.window.geometry("900x630")

        self.nodes = []
        self.edges = []

        self.selected_node = None
        self.drag_mode = None
        self.is_directed = False

        self.original_x = 0
        self.original_y = 0

        self.canvas = tk.Canvas(self.window, bg="white", width = 850, height = 550)
        self.canvas.grid(row =0, column=0, padx = 20, pady = 20)

        self.directed_var = tk.BooleanVar(value = self.is_directed)
        self.directed_checkbox = tk.Checkbutton(
            self.window,
            text = "Directed graph",
            variable = self.directed_var,
            command = self.toggle_directed_mode,
            font = ("Arial", 10, "bold")
        )
        self.directed_checkbox.grid(row =1, column = 0, sticky = "w", padx = 20, pady = (0,10))

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<Button-3>", self.on_right_click)

        self.save_adjacency_matrix()

    def calculate_distance(self, x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def clamp_coordinates(self, x, y, radius = 20, padding = 10):
        margin = radius + padding

        clamped_x = max(margin, min(x, 850 - margin))
        clamped_y = max(margin, min(y, 550 - margin))
        return clamped_x, clamped_y

    def toggle_directed_mode(self):
        self.is_directed = self.directed_var.get()

        for edge in self.edges:
            edge.is_directed = self.is_directed

        self.redraw_canvas()
        self.save_adjacency_matrix()

    def redraw_canvas(self, temp_line_coords = None):
        self.canvas.delete("all")

        for edge in self.edges:
            edge.draw(self.canvas)

        if temp_line_coords:
            x1, y1, x2, y2 = temp_line_coords
            arrow_style = tk.LAST if self.is_directed else tk.NONE
            self.canvas.create_line(
                x1, y1, x2, y2,
                fill = "gray", width = 2,
                dash = (4,4), arrow = arrow_style
            )

        for node in self.nodes:
            node.draw(self.canvas)

    def on_mouse_down(self, event):
        x, y = self.clamp_coordinates(event.x, event.y)

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
            return

        near_node = None
        tolerance = 20
        for node in self.nodes:
            dist = self.calculate_distance(node.x, node.y, x, y)
            if node.radius < dist <= (node.radius + tolerance):
                near_node = node
                break

        if near_node is not None:
            self.selected_node = near_node
            self.drag_mode = "create_edge"
            return

        too_close = False
        min_distance = 40
        for node in self.nodes:
            dist = self.calculate_distance(node.x, node.y, x, y)
            if dist < (node.radius * 2 + min_distance):
                too_close = True
                break

        if too_close:
            messagebox.showwarning(title="Collision warning", message = "Cannot place a node too close or on top of another node!")
            return

        self.selected_node = None
        self.drag_mode = None

        if self.nodes:
            new_id = max(node.id for node in self.nodes) + 1
        else:
            new_id = 1

        new_node = Node(new_id, x, y)

        new_node.draw(self.canvas)
        self.nodes.append(new_node)
        self.save_adjacency_matrix()

    def on_mouse_drag(self, event):
        if self.drag_mode == "move_node" and self.selected_node is not None:
            x, y = self.clamp_coordinates(event.x, event.y)
            self.selected_node.x = x
            self.selected_node.y = y
            self.redraw_canvas()

        elif self.drag_mode == "create_edge" and self.selected_node is not None:
            self.redraw_canvas(temp_line_coords = (self.selected_node.x, self.selected_node.y, event.x, event.y))

    def on_mouse_up(self, event):
        if self.drag_mode == "move_node" and self.selected_node is not None:
            collision = False
            min_distance = 40
            for node in self.nodes:
                if node != self.selected_node:
                    dist = self.calculate_distance(node.x, node.y, self.selected_node.x, self.selected_node.y)
                    if dist < (self.selected_node.radius * 2 + min_distance):
                        collision = True
                        break

            if collision:
                self.selected_node.x = self.original_x
                self.selected_node.y = self.original_y
                messagebox.showwarning(title="Collision warning",
                                       message="Cannot place a node too close or on top of another node!")
            self.redraw_canvas()
            self.save_adjacency_matrix()

        elif self.drag_mode == "create_edge" and self.selected_node is not None:
            target_node = None
            tolerance = 20
            x, y = event.x, event.y

            for node in self.nodes:
                if node != self.selected_node:
                    dist = self.calculate_distance(node.x, node.y, x, y)
                    if dist <= (node.radius + tolerance):
                        target_node = node
                        break

            if target_node is not None:
                edge_exists = False
                for edge in self.edges:
                    if edge.connects(self.selected_node, target_node):
                        edge_exists = True
                        break

                if not edge_exists:
                    new_edge = Edge(self.selected_node, target_node, self.is_directed)
                    self.edges.append(new_edge)
                    self.save_adjacency_matrix()
                else:
                    messagebox.showwarning(title="Edge warning", message = "Edge already exists between these nodes!")

            else:
                messagebox.showwarning(title="Edge warning", message = "Edge must end near another node!")

            self.redraw_canvas()

        self.selected_node = None
        self.drag_mode = None

    def on_right_click(self, event):
        x, y = event.x, event.y
        node_to_delete = None

        for node in self.nodes:
            if node.contains_point(x, y):
                node_to_delete = node
                break

        if node_to_delete is not None:
            self.edges = [edge for edge in self.edges if edge.node1 != node_to_delete and edge.node2 != node_to_delete]
            self.nodes.remove(node_to_delete)
            self.redraw_canvas()
            self.save_adjacency_matrix()

    def save_adjacency_matrix(self, filename = "adjacency_matrix.txt"):
        n = len(self.nodes)

        sorted_nodes = sorted(self.nodes, key = lambda node: node.id)

        id_to_index = {}
        for index, node in enumerate(sorted_nodes):
            id_to_index[node.id] = index

        matrix = []
        for i in range(n):
            row = [0] * n
            matrix.append(row)

        for edge in self.edges:
            id1 = edge.node1.id
            id2 = edge.node2.id

            u = id_to_index[id1]
            v = id_to_index[id2]

            if self.is_directed:
                matrix[u][v] = 1
            else:
                matrix[u][v] = 1
                matrix[v][u] = 1

        try:
            with open(filename, "w") as f:
                f.write(f"{n}\n")
                for row in matrix:
                    row_string = " ".join(map(str,row))
                    f.write(row_string + "\n")
        except Exception as e:
            print(e)