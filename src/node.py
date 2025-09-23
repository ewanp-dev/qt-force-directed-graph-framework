from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsItem


class FDNode(QGraphicsEllipseItem):
    """
    contains the single node object for the node graph
    """

    def __init__(self, title: str = "", width=100, height=100) -> None:
        """
        constructor

        :param title: The title given to the node, will also be used as a label for the node
        :parm width: The width of the node, keep default for now
        :param height: The height of the node, keep default for now and the same as width for a circle
        """
        super().__init__(0, 0, width, height)

        self.title: str = title

        # NOTE this is going to be put into an argument or globals at a later date1
        COL_SUBLAYER: str = "#0000ff"
        COL_REFERENCE: str = "#00ff00"
        COL_PAYLOAD: str = "#ff0000"

        self.setBrush(QBrush(QColor(COL_SUBLAYER)))  # temp sublayer color
        self.setPen(QPen(QColor(COL_REFERENCE), 2))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
