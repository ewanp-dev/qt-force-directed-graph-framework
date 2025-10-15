#include <QApplication>
#include <QPushButton>
#include <cstdlib>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    // TODO: Create a dependency network (all stemming from one node)
    // TODO: Add node input highlighting

    QApplication app (argc, argv);

    ForceDirectedGraph* graph = new ForceDirectedGraph();
    graph->resize(1200,800);

    int ROWS = 30;
    int COLUMNS = 30;
    int GAP=10;

    std::vector<Node*> createdNodes;
    for (int row = 0; row  < ROWS; row++) {
        for (int column = 0; column < COLUMNS; column++) {
            Node* newNode = graph->addNode(std::to_string(row));
            newNode->setPos(row * GAP, column * GAP);

            if (createdNodes.size() > 0) {
                int index = std::rand() % createdNodes.size();

                Node* connectedNode = createdNodes[index];
                graph->connectNodes(newNode, connectedNode);
            }

            createdNodes.push_back(newNode);
        }
    }

    graph->show();

    return app.exec();
}
