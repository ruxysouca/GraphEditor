# Graph Editor (Python & Tkinter)

An interactive graph editor built in Python using Tkinter, designed for creating, manipulating and exporting directed and undirected graphs.

## Project Goal
The primary goal of this project is to provide a robust, visual tool for building and manipulating graph data structures. It serves as an interactive bridge between the visual representation of a graph and its mathematical foundation, ensuring that any graphical modifications are instantly reflected in a perfectly synchronized adjacency matrix.

## Features & Requirements Implemented

1. **Dynamic Node Creation**: left-clicking on empty canvas space creates a new node with auto-incremented ID.
2. **Collision Detection**: prevents node overlapping by detecting proximity and snapping back with a warning message.
3. **Edge Creation**: dragging from the border of one node to another successfully connects them with an edge.
4. **File Persistence**: automatically saves the adjacency matrix to `adjacency_matrix.txt` on every single change (node creation, edge addition, node dragging or deletion). The first row contains the number of nodes, followed by the matrix rows.
5. **Directed & Undirected Support**:
  * toggle between directed and undirected modes via a checkbox.
  * supports independent bi-directional arcs in directed graphs.
  * dynamic conversion of existing edges when toggling modes on the fly.
6. **Node Repositioning (Drag-and-Drop)**: freely drag nodes around the canvas while connected edges update in real-time.
7. **Quick Deletion**: right-clicking a node instantly removes it along with all its connected edges.
8. **Canvas Boundary Constraining**: limits node coordinates with a custom padding, preventing nodes from being created or dragged outside the visible canvas area.
9. **Clear All Functionality**: a dedicated button with a safety confirmation dialog to instantly clear the entire canvas, reset lists, and empty the adjacency matrix.

## Project Structure

* `main.py` -> application entry point that initializes the main window.
* `graph_editor.py` -> core editor logic, canvas bindings, state management and adjacency matrix export.
* `node.py` -> defines node properties, rendering, and distance/collision math.
* `edge.py` -> handles edge rendering (lines and arrowheads) and connection logic.
* `adjacency_matrix.txt` -> dynamically generated file containing the graph's adjacency matrix.
