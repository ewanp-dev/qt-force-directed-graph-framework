from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget

from .GraphicsScene import GraphicsScene
from .GraphicsView import GraphicsView
from .Node import Node
from .Edge import Edge

class ForceDirectedGraph(QWidget):
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
        self.graphics_scene = GraphicsScene()
        self.view: GraphicsView = GraphicsView(self.graphics_scene, self)
        _lyt.addWidget(self.view)

    def createNode(
        self, x: float = 0.0, y: float = 0.0, node_name: str = "node"
    ) -> Node:
        """
        Creates a new node on the graph.

        Returns:
            FDNode: Newly created node.
        """

        return self.view.createNode()

    def connectNodes(self, start_node, end_node):
        self.graphics_scene.addItem(Edge(start_node, end_node))

