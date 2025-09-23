from PyQt6.QtWidgets import QWidget

from view import FDGraphicsView


class FDNodeGraphWidget(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.initUI()

    def initUI(self) -> None:
        self.view: FDGraphicsView = FDGraphicsView()
        return None
