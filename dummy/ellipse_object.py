import sys

from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QBrush, QPen
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsScene,
    QGraphicsView,
)


class DraggableEllipse(QGraphicsEllipseItem):
    def __init__(self, rect, pen, brush):
        super().__init__(rect)
        self.setPen(pen)
        self.setBrush(brush)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(
            QGraphicsEllipseItem.GraphicsItemFlag.ItemSendsScenePositionChanges
        )

    def itemChange(self, change, value):
        if change == QGraphicsEllipseItem.GraphicsItemChange.ItemPositionHasChanged:
            pos = self.pos()
            print(f"Ellipse moved to: x={pos.x():.2f}, y={pos.y():.2f}")
        return super().itemChange(change, value)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    scene = QGraphicsScene()
    view = QGraphicsView(scene)

    pen = QPen(Qt.GlobalColor.black)
    brush = QBrush(Qt.GlobalColor.green)

    ellipse = DraggableEllipse(QRectF(-100, -100, 100, 100), pen, brush)
    scene.addItem(ellipse)

    view.show()
    sys.exit(app.exec())
