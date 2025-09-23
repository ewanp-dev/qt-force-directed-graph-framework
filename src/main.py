from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget

from view import FDGraphicsView


class FDNodeGraphWidget(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.initUI()

    def initUI(self) -> None:
        _lyt = QVBoxLayout(self)
        self.view: FDGraphicsView = FDGraphicsView()
        _lyt.addWidget(self.view)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    graph = FDNodeGraphWidget()
    graph.setWindowTitle("Node Graph")
    graph.resize(800, 800)
    graph.show()
    sys.exit(app.exec())
