from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsItem, QGraphicsLineItem


class FDNode(QGraphicsEllipseItem):
    """
    contains the single node object for the node graph
    """

    def __init__(self, x, y, r, color="#3498DB") -> None:
        """
        constructor

        :param title: The title given to the node, will also be used as a label for the node
        :parm width: The width of the node, keep default for now
        :param height: The height of the node, keep default for now and the same as width for a circle
        """
        super().__init__(-r, -r, 2 * r, 2 * r)

        self.connections = []
        self.setBrush(QBrush(QColor(color)))  # temp sublayer color
        self.setPen(QPen(Qt.GlobalColor.black, 2))
        self.setFlag(self.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(self.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(self.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setPos(x, y)

    def center(self) -> QPointF:
        return self.scenePos()

    def add_connection(self, connection) -> None:
        """
        Adds the line class to the connections list for later use

        :param connection: The QGraphicsLineItem class connection
        """
        self.connections.append(connection)

    def itemChange(self, change, value) -> None:
        """
        Updates the position of the line once a node is moved

        :param change: The change type of the node
        :param value:
        """
        if change == self.GraphicsItemChange.ItemPositionHasChanged:
            for conn in self.connections:
                conn.update_position()
        return super().itemChange(change, value)


class Connect(QGraphicsLineItem):
    """
    The graphics line connection between nodes
    """

    def __init__(self, node_a: FDNode, node_b: FDNode) -> None:
        """
        Constructor

        :param node_a: The input node
        :param node_b: The node to connect to
        """
        super().__init__()
        self.node_a = node_a
        self.node_b = node_b
        self.setPen(QPen(QColor("#F1C40F"), 2))
        self.setZValue(-1)
        node_a.add_connection(self)
        node_b.add_connection(self)
        self.update_position()

    def update_position(self):
        """
        Updates the line position when the node object is moved
        """
        self.setLine(
            self.node_a.center().x(),
            self.node_a.center().y(),
            self.node_b.center().x(),
            self.node_b.center().y(),
        )
