import math
import random
import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsScene,
    QGraphicsView,
)


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
        self.k = 100  # "ideal" edge length
        self.cooling = 0.85

        # Create nodes as graphics items
        for node in nodes:
            x, y = random.randint(-200, 200), random.randint(-200, 200)
            item = QGraphicsEllipseItem(-15, -15, 30, 30)
            item.setBrush(QBrush(Qt.GlobalColor.cyan))
            item.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
            self.scene.addItem(item)
            self.nodes[node] = item
            self.positions[node] = [x, y]
            self.velocities[node] = [0, 0]

        # Draw edges (store refs for redraw)
        self.edge_items = []
        for u, v in edges:
            line = self.scene.addLine(0, 0, 0, 0, QPen(Qt.GlobalColor.gray, 2))
            self.edge_items.append((u, v, line))

        # Timer for simulation
        self.timer = QTimer()
        self.timer.timeout.connect(self.step)
        self.timer.start(30)

    def step(self):
        forces = {n: [0, 0] for n in self.nodes}

        # Repulsive forces
        for u in self.nodes:
            for v in self.nodes:
                if u == v:
                    continue
                dx = self.positions[u][0] - self.positions[v][0]
                dy = self.positions[u][1] - self.positions[v][1]
                dist = math.sqrt(dx * dx + dy * dy) + 0.01
                force = self.k * self.k / dist
                forces[u][0] += (dx / dist) * force
                forces[u][1] += (dy / dist) * force

        # Attractive forces
        for u, v in self.edges:
            dx = self.positions[u][0] - self.positions[v][0]
            dy = self.positions[u][1] - self.positions[v][1]
            dist = math.sqrt(dx * dx + dy * dy) + 0.01
            force = (dist * dist) / self.k
            forces[u][0] -= (dx / dist) * force
            forces[u][1] -= (dy / dist) * force
            forces[v][0] += (dx / dist) * force
            forces[v][1] += (dy / dist) * force

        # Update positions (with cooling)
        for n in self.nodes:
            self.velocities[n][0] = (
                self.velocities[n][0] + forces[n][0]
            ) * self.cooling
            self.velocities[n][1] = (
                self.velocities[n][1] + forces[n][1]
            ) * self.cooling
            self.positions[n][0] += self.velocities[n][0] * 0.01
            self.positions[n][1] += self.velocities[n][1] * 0.01

            # Update graphics
            self.nodes[n].setPos(self.positions[n][0], self.positions[n][1])

        # Update edges
        for u, v, line in self.edge_items:
            x1, y1 = self.positions[u]
            x2, y2 = self.positions[v]
            line.setLine(x1, y1, x2, y2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    nodes = ["A", "B", "C", "D", "E"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

    viewer = ForceDirectedGraph(nodes, edges)
    viewer.setWindowTitle("Force-Directed Graph (No External Libs)")
    viewer.resize(800, 600)
    viewer.show()

    sys.exit(app.exec())
