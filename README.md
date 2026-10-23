# Graph Editor (Python & Tkinter)

An interactive graph editor built in Python using Tkinter, designed for creating, manipulating and exporting directed and undirected graphs.


## Features & Requirements Implemented

1. **Dynamic Node Creation**: left-clicking on empty canvas space creates a new node with auto-incremented ID.
2. **Collision Detection**: prevents node overlapping by detecting proximity and snapping back with a warning message.
3. **Edge Creation**: dragging form the border of one node to another successfully connects them with an edge.
4. **File Persistence**: automatically saves the adjacency matrix to `adjacency_matrix.txt` on every single change (node creation, edge addition, node dragging or deletion). The first row contains the number of nodes, followed by the matrix rows.
5. **Directed & Undirected Support**:
  * toggle between directed and undirected modes via a checkbox.
  * supports independent bi-directional arcs in directed graphs.
  * dynamic conversion of existing edges when toggling modes on the fly.
6. **Node Repositioning (Drag-and-Drop)**: freely drag nodes around the canvas while connected edges update in real-time.
7. **Quick Deletion**: right-clicking a node instantly removes it along with all its connected edges.

## Project Structure

* `main.py` -> application entry point that initializes the main window.
* `graph_editor.py` -> core editor logic, canvas bindings, state management and adjacency matrix export.
* `node.py` -> defines node properties, rendering, and distance/collision math.
* `edge.py` -> handles edge rendering (lines and arrowheads) and connection logic.
* `adjacency_matrix.txt` -> dynamically generated file containing the graph's adjacency matrix.
