from PyQt6.QtGui import QBrush, QColor, QPainter, QPainterPath, QPen
from PyQt6.QtWidgets import (
    QGraphicsLineItem,
)
from .Node import Node

class Edge(QGraphicsLineItem):
    """
    The graphics line connection between nodes
    """

    def __init__(self, node: Node, input: Node) -> None:
        """
        Constructor

        :param node_a: The input node
        :param node_b: The node to connect to
        """
        super().__init__()
        self.node = node
        self.input = input
        self.__default_color: str = "#2c2f33"
        self.setPen(QPen(QColor(self.__default_color), 2))
        self.setZValue(-1)
        node.add_connection(self)
        input.add_connection(self)
        self.update_position()

    def update_position(self):
        """
        Updates the line position when the node object is moved
        """
        self.setLine(
            self.node.center().x(),
            self.node.center().y(),
            self.input.center().x(),
            self.input.center().y(),
        )

    def setLineColor(self, color: str) -> None:
        """
        Sets the color of a line connecting a node

        :param color: The hex color code of the line
        """
        self.setPen(QPen(QColor(color), 2))

    def setDefaultColor(self) -> None:
        """
        Reverts the line back to its default color
        """
        self.setPen(QPen(QColor(self.__default_color), 2))

