from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget

try:
    from scene import FDGraphicsScene
    from view import FDGraphicsView
except ModuleNotFoundError:
    from .scene import FDGraphicsScene
    from .view import FDGraphicsView


class FDNodeGraphWidget(QWidget):
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


if __name__ == "__main__":
    """
    TODO
    -- remove need for parent argument on connect node
    -- add in method for auto layout of nodes
    """
    import sys

    app = QApplication(sys.argv)
    graph = FDNodeGraphWidget()
    viewer = graph.view
    node_a = viewer.createNode(node_name="Something")
    node_b = viewer.createNode()
    node_b.setName("node_a_name")
    node_b.setPosition(-100, -50)
    node_a.setInput(parent=viewer, input=node_b)
    graph.setWindowTitle("Node Graph")
    graph.resize(800, 800)
    graph.show()
    sys.exit(app.exec())
