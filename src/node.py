from typing import List, Optional

from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen
from PyQt6.QtWidgets import (
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsLineItem,
    QGraphicsSceneHoverEvent,
    QGraphicsSceneMouseEvent,
    QGraphicsView,
    QStyleOptionGraphicsItem,
    QWidget,
)


class FDNode(QGraphicsEllipseItem):
    """
    contains the single node object for the node graph
    """

    def __init__(self, x: float, y: float, r: float = 20.0) -> None:
        """
        constructor

        :param title: The title given to the node, will also be used as a label for the node
        :parm width: The width of the node, keep default for now
        :param height: The height of the node, keep default for now and the same as width for a circle
        """
        super().__init__(-r, -r, 2 * r, 2 * r)

        self.__node_color: str = "#bec4cf"
        self.__hover_color: str = "#c9bf99"
        self.__current_color = self.__node_color
        self.connections = []

        self.x: float = x
        self.y: float = y
        self.setFlag(self.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(self.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(self.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.setPos(x, y)

    def center(self) -> QPointF:
        return self.scenePos()

    def paint(
        self,
        painter: QPainter | None,
        option: QStyleOptionGraphicsItem | None,
        widget: QWidget | None = None,
    ) -> None:
        """
        Paint event, removes selection outline
        """
        painter.setBrush(QBrush(QColor(self.__current_color)))
        painter.setPen(QPen(QColor(self.__current_color), 2))
        painter.drawEllipse(self.rect())

    def hoverEnterEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        """
        The method that executes when a node is being hovered over

        :param event: The event type
        """
        self.__current_color = self.__hover_color
        self.setCursor(Qt.CursorShape.OpenHandCursor)
        self.update()
        return super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event: QGraphicsSceneHoverEvent) -> None:
        self.__current_color = self.__node_color
        self.unsetCursor()
        self.update()
        return super().hoverLeaveEvent(event)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        """
        Method containing code that executes when the mouse is pressed on a node

        :param event: The type of mouse press event
        """
        if event.button() != Qt.MouseButton.LeftButton:
            return super().mousePressEvent(
                event
            )  # only supporting LMB for now, will update later
        else:
            # LMB button click execution code
            pass

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        """
        Method that executes when the mouse button is released

        :param event: The mouse event
        """

        # need to set this otherwise the node stays selected, moving the line constantly
        self.setSelected(False)
        return super().mouseReleaseEvent(event)

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
            self.setSelected(False)
            for conn in self.connections:
                conn.update_position()
        return super().itemChange(change, value)

    def setInput(self, parent: QGraphicsView, input: QGraphicsEllipseItem) -> None:
        """
        Sets the node input

        :param parent: The node graph instance where the node lives
        :param input: The node to input to the current node
        """
        parent.scene().addItem(Connect(self, input))

    def setInputs(self, inputs: List[QGraphicsEllipseItem]) -> None:
        if not inputs:
            return

    def inputs(self) -> List[QGraphicsEllipseItem]:
        """
        Returns a list of inputs connected to the node
        """
        return [i.input for i in self.connections if self.connections]

    def setPosition(self, x: float, y: float) -> None:
        """
        Sets the position of the node

        :param x: The position on the x axis
        :param y: The position on the y axis
        """
        self.setPos(x, y)

    def setNodeRadius(self, radius: float) -> None:
        """
        Sets the radius of the node, currently setting it to a stupid high value breaks the graph

        :param radius: The radius of the node
        """
        if radius < 0.001:
            radius = 0.001
        elif radius > 150:
            radius = 150

        self.setRect(-radius / 2, -radius / 2, radius, radius)
        return None


class Connect(QGraphicsLineItem):
    """
    The graphics line connection between nodes
    """

    def __init__(self, node: FDNode, input: FDNode) -> None:
        """
        Constructor

        :param node_a: The input node
        :param node_b: The node to connect to
        """
        super().__init__()
        self.node = node
        self.input = input
        self.setPen(QPen(QColor("#2c2f33"), 2))
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
