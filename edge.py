class Edge:

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def connect(self, node1, node2):
        return (self.node1 == node1 and self.node2 == node2) or (self.node1 == node2 and self.node2 == node1)

    