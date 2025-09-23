from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QGraphicsView

from scene import FDGraphicsScene


class FDGraphicsView(QGraphicsView):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.TextAntialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )
        self.setScene(FDGraphicsScene())
        self.setSceneRect(-500, -500, 1000, 1000)
        self.setDragMode(QGraphicsView.DragMode.RubberBandDrag)
