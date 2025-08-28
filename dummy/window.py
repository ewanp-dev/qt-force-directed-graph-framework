from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import (
    QGraphicsItem,
    QGraphicsScene,
    QGraphicsView,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from graphics_scene import ForceDirectedGraphicsScene
from graphics_view import ForceDirectedGraphicsView


class ForceDrivenNodeEditorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Node Editor Dummy")
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()

        # add this into an argument
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # create graphics scene
        self.graphics_scene = ForceDirectedGraphicsScene()

        # graphics view
        # need to make the parent be dynamic
        self.view = ForceDirectedGraphicsView(self.graphics_scene, self)
        self.layout.addWidget(self.view)

        self.show()

        self.add_debug_content()

    def add_debug_content(self):
        # adding a green rectangle as a test
        green_brush = QBrush(Qt.GlobalColor.green)
        outline_pen = QPen(Qt.GlobalColor.black)
        outline_pen.setWidth(2)

        """
        it is going to be very important to remember this function as it
        will be the main one when setting out the force direction
        """
        # rectangle = self.graphics_scene.addRect(
        #    -100, -100, 80, 100, outline_pen, green_brush
        # )
        # rectangle.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        # rectangle.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        ellipse = self.graphics_scene.addEllipse(
            -100, -100, 100, 100, outline_pen, green_brush
        )
        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        text = self.graphics_scene.addText("This is a sample text")
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        # adding widget
        widget = QPushButton("Test Button")
        proxy = self.graphics_scene.addWidget(widget)
        proxy.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        proxy.setPos(0, 30)

        line = self.graphics_scene.addLine(-200, -200, 400, -100, outline_pen)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
