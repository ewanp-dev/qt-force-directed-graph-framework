#include <QApplication>
#include <QPushButton>
#include <cstdlib>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    int ROWS = 5;
    int COLUMNS = 5;
    int GAP = 20;

    fdg::ForceDirectedGraph* graph = new fdg::ForceDirectedGraph();

    std::vector<fdg::Node*> createdNodes;
    for(int row=0; row<ROWS; row++)
    {
        for(int column=0; column<COLUMNS; column++)
        {
            fdg::Node* newNode = graph->addNode("foo");
            newNode->setPos(row*GAP, column*GAP);

            // connect node
            if(createdNodes.size()>0)
            {
                int index = std::rand() % createdNodes.size();
                fdg::Node* connectedNode = createdNodes[index];

                graph->connectNodes(newNode, connectedNode);
            }

            createdNodes.push_back(newNode);
        }

    }


    graph->show();

    return app.exec();
}
