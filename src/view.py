from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView

from node import FDNode
from scene import FDGraphicsScene


class FDGraphicsView(QGraphicsView):

    def __init__(self) -> None:
        super().__init__()
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.TextAntialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )
        self.setScene(FDGraphicsScene())
        self.setSceneRect(-500, -500, 1000, 1000)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)

        # temp node creation for test
        node_a: FDNode = FDNode(title="test_string")
        node_a.setPos(100, 0)
        self.scene().addItem(node_a)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    graph = FDGraphicsView()
    graph.setWindowTitle("Node Graph")
    graph.resize(800, 800)
    graph.show()
    sys.exit(app.exec())
