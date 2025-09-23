import sys

from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,
)


class NodeSocket(QGraphicsEllipseItem):
    def __init__(self, parent, position: QPointF):
        super().__init__(-5, -5, 10, 10, parent)
        self.setBrush(QBrush(QColor("#2E86C1")))
        self.setPen(QPen(Qt.PenStyle.NoPen))
        self.setPos(position)


class Node(QGraphicsEllipseItem):
    def __init__(self, title: str, width=120, height=60):
        super().__init__(0, 0, width, height)
        self.setBrush(QBrush(QColor("#1B2631")))
        self.setPen(QPen(QColor("#34495E"), 2))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.title = title

        NodeSocket(self, QPointF(0, height / 2))  # Input socket
        NodeSocket(self, QPointF(width, height / 2))  # Output socket


class NodeGraph(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.TextAntialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )
        self.setScene(QGraphicsScene())
        self.setSceneRect(-500, -500, 1000, 1000)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)

        node_a = Node("Node A")
        node_a.setPos(-150, -50)
        self.scene().addItem(node_a)

        node_b = Node("Node B")
        node_b.setPos(100, 0)
        self.scene().addItem(node_b)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = NodeGraph()
    graph.setWindowTitle("Node Graph")
    graph.resize(800, 600)
    graph.show()
    sys.exit(app.exec())
