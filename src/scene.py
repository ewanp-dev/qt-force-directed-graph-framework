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

        self._background_color = QColor("#393939")

        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(
            -self.scene_width // 2,
            -self.scene_height // 2,
            self.scene_width,
            self.scene_height,
        )
        self.setBackgroundBrush(self._background_color)
