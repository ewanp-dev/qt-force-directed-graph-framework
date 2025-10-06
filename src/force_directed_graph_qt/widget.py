from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget

try:
    from scene import FDGraphicsScene
    from view import FDGraphicsView
except ModuleNotFoundError:
    from .scene import FDGraphicsScene
    from .view import FDGraphicsView


class FDGraphWidget(QWidget):
    """
    The standard FD node graph widget
    """

    def __init__(self, parent=None) -> None:
        """
        Constructor

        :param parent: The qt parent object
        """
        super().__init__(parent)

        self.initUI()

    def initUI(self) -> None:
        """
        UI Constructor
        """

        self.setContentsMargins(0, 0, 0, 0)
        _lyt = QVBoxLayout(self)
        _lyt.setContentsMargins(0, 0, 0, 0)
        self.graphics_scene = FDGraphicsScene()
        self.view: FDGraphicsView = FDGraphicsView(self.graphics_scene, self)
        _lyt.addWidget(self.view)

