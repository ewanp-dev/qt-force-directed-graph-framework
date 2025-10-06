from force_directed_graph_qt import FDGraphWidget
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget

import sys

app = QApplication(sys.argv)
graph = FDGraphWidget()
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
