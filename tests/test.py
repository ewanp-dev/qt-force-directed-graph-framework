import math
import random
import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsLineItem,
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
)


class Node(QGraphicsEllipseItem):
    def __init__(self, name, x, y, graph, radius=20):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius)
        self.setBrush(QBrush(Qt.GlobalColor.yellow))
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(
            QGraphicsEllipseItem.GraphicsItemFlag.ItemSendsScenePositionChanges
        )
        self.setPos(x, y)

        self.name = name
        self.graph = graph

        # 🔹 Add a text label that follows this node
        self.label = QGraphicsTextItem(name, self)
        self.label.setDefaultTextColor(Qt.GlobalColor.black)
        self.label.setPos(-radius / 2, -radius / 2)

    def itemChange(self, change, value):
        if change == QGraphicsEllipseItem.GraphicsItemChange.ItemPositionChange:
            self.graph.update_edges()
        return super().itemChange(change, value)


class ForceDirectedGraph(QGraphicsView):
    def __init__(self, nodes, edges):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.nodes = {}
        self.positions = {}
        self.velocities = {}
        self.edges = edges

        # Parameters
        self.k = 120  # Ideal distance
        self.cooling = 0.85

        # 🔹 Define edges container early so it's safe
        self.edge_items = []

        # Create nodes
        for node in nodes:
            x, y = random.randint(-200, 200), random.randint(-200, 200)
            item = Node(node, x, y, self)
            self.scene.addItem(item)
            self.nodes[node] = item
            self.positions[node] = [x, y]
            self.velocities[node] = [0, 0]

        # Create edges
        for u, v in edges:
            line = self.scene.addLine(0, 0, 0, 0, QPen(Qt.GlobalColor.gray, 2))
            self.edge_items.append((u, v, line))

        # Timer for simulation
        self.timer = QTimer()
        self.timer.timeout.connect(self.step)
        self.timer.start(30)

    def update_edges(self):
        if not hasattr(self, "edge_items"):
            return
        for u, v, line in self.edge_items:
            x1, y1 = self.nodes[u].pos().x(), self.nodes[u].pos().y()
            x2, y2 = self.nodes[v].pos().x(), self.nodes[v].pos().y()
            line.setLine(x1, y1, x2, y2)

    def step(self):
        width, height = 800, 600
        forces = {node: [0, 0] for node in self.nodes}

        # Repulsive forces
        for u in self.nodes:
            for v in self.nodes:
                if u == v:
                    continue
                dx = self.nodes[u].pos().x() - self.nodes[v].pos().x()
                dy = self.nodes[u].pos().y() - self.nodes[v].pos().y()
                dist = math.sqrt(dx * dx + dy * dy) + 0.01
                repulse = self.k * self.k / dist
                forces[u][0] += (dx / dist) * repulse
                forces[u][1] += (dy / dist) * repulse

        # Attractive forces
        for u, v in self.edges:
            dx = self.nodes[u].pos().x() - self.nodes[v].pos().x()
            dy = self.nodes[u].pos().y() - self.nodes[v].pos().y()
            dist = math.sqrt(dx * dx + dy * dy) + 0.01
            attract = (dist * dist) / self.k
            forces[u][0] -= (dx / dist) * attract
            forces[u][1] -= (dy / dist) * attract
            forces[v][0] += (dx / dist) * attract
            forces[v][1] += (dy / dist) * attract

        # Update positions
        for node in self.nodes:
            fx, fy = forces[node]
            self.velocities[node][0] = (self.velocities[node][0] + fx) * self.cooling
            self.velocities[node][1] = (self.velocities[node][1] + fy) * self.cooling
            x = self.nodes[node].pos().x() + self.velocities[node][0] * 0.01
            y = self.nodes[node].pos().y() + self.velocities[node][1] * 0.01
            self.nodes[node].setPos(x, y)

        self.update_edges()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    nodes = ["A", "B", "C", "D", "E"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

    window = ForceDirectedGraph(nodes, edges)
    window.setWindowTitle("Force-Directed Graph (Drag nodes!)")
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
