from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QPainter, QWheelEvent
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView

from node import Connect, FDNode


class FDGraphicsView(QGraphicsView):
    """
    The main nodegraph view
    """

    def __init__(self, scene, parent=None) -> None:
        """
        Constructor

        :param scene: The external graphics scene
        :param parent: The qt parent object
        """
        super().__init__(parent)
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.TextAntialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )
        self.graphics_scene = scene
        self.setScene(self.graphics_scene)
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self._last_mouse_pos: float | None = None
        self._zoom_factor: float = 1.15
        self._min_zoom: float = 0.1
        self._max_zoom: float = 10.0
        self._current_zoom: float = 1.0

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Getting the position of the mouse after MMB

        :param event: Input mouse event
        """
        if event.button() == Qt.MouseButton.MiddleButton:
            self._last_mouse_pos = event.pos()
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Moving the nodegraph position after MMB and moving

        :param event: The input mouse event
        """
        if self._last_mouse_pos is not None:
            delta = event.pos() - self._last_mouse_pos
            self._last_mouse_pos = event.pos()
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Gets rid of the mouse position upon release of the MMB

        :param event: The input mouse event
        """
        if event.button() == Qt.MouseButton.MiddleButton:
            self._last_mouse_pos = None
            event.accept()
        else:
            super().mouseReleaseEvent(event)

    def wheelEvent(self, event: QWheelEvent) -> None:
        """
        Zooms in and out of the node graph based on the mouse
        position

        :param event: The input wheel event
        """
        old_pos = self.mapToScene(event.position().toPoint())

        zoom_out = event.angleDelta().y() < 0
        if zoom_out:
            factor = 1 / self._zoom_factor
        else:
            factor = self._zoom_factor

        new_zoom = self._current_zoom * factor
        if self._min_zoom <= new_zoom <= self._max_zoom:
            self._current_zoom = new_zoom
            self.scale(factor, factor)

            new_pos = self.mapToScene(event.position().toPoint())

            delta = new_pos - old_pos
            self.translate(delta.x(), delta.y())

    def createNode(
        self, x: float = 0.0, y: float = 0.0, node_name: str = "node"
    ) -> FDNode:
        """
        Creates a node on the graph
        """
        node: FDNode = FDNode(x=x, y=y, node_name=node_name)
        self.scene().addItem(node)
        return node


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    graph = FDGraphicsView(scene=QGraphicsScene)

    graph.setWindowTitle("Node Graph")
    graph.resize(800, 800)
    graph.show()
    sys.exit(app.exec())
