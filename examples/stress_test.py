from force_directed_graph_qt import ForceDirectedGraph
from PyQt6.QtWidgets import QApplication

import sys
import random

app = QApplication(sys.argv)
graph = ForceDirectedGraph()

# setup window
graph.setWindowTitle("Node Graph")
graph.resize(800, 800)

# create nodes
ROWS = 20
COLUMNS = 20
GAP = 100

created_nodes = []

for row in range(ROWS):
    for column in range(COLUMNS):
        new_node = graph.createNode()
        new_node.setPosition(row*GAP, column*GAP)

        # connect node
        if(len(created_nodes)>0):
            index = random.randint(0, len(created_nodes)-1)
            connected_node = created_nodes[index]

            graph.connectNodes(new_node, connected_node)

        created_nodes.append(new_node)


# conections
# graph.connectNodes(node_a, node_b)

graph.show()
sys.exit(app.exec())
