from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget

from .scene import FDGraphicsScene
from .view import FDGraphicsView
from .node import Edge, FDNode

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

    def createNode(
        self, x: float = 0.0, y: float = 0.0, node_name: str = "node"
    ) -> FDNode:
        """
        Creates a new node on the graph.

        Returns:
            FDNode: Newly created node.
        """

        return self.view.createNode()

    def connectNodes(self, start_node, end_node):
        self.graphics_scene.addItem(Edge(start_node, end_node))

