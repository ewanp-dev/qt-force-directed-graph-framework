from force_directed_graph_qt import ForceDirectedGraph
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget

import sys

app = QApplication(sys.argv)
graph = ForceDirectedGraph()

# setup window
graph.setWindowTitle("Node Graph")
graph.resize(800, 800)

# create nodes
node_a = graph.createNode(node_name="Something")
node_b = graph.createNode()

# configure node_b
node_b.setName("node_a_name")
node_b.setPosition(-100, -50)

# conections
graph.connectNodes(node_a, node_b)

graph.show()
sys.exit(app.exec())
