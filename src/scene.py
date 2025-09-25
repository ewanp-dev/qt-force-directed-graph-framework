from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QGraphicsScene


class FDGraphicsScene(QGraphicsScene):
    """
    Contains all of the settings for the nodegraph scene
    """

    def __init__(self, parent=None) -> None:
        """
        Constructor

        :param parent: The parent Qt object
        """
        super().__init__(parent)

        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(
            -self.scene_width // 2,
            -self.scene_height // 2,
            self.scene_width,
            self.scene_height,
        )
        self.setBackgroundColor("#1c2026")

    def setBackgroundColor(self, color: str) -> None:
        """
        Set the background color of the nodegraph
        """
        self.setBackgroundBrush(QColor(color))
