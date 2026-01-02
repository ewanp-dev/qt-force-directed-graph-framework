#include <QApplication>
#include <QPushButton>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    fdg::ForceDirectedGraph* graph = new fdg::ForceDirectedGraph();
    fdg::Node* nodeA = graph->addNode("Hello World");
    fdg::Node* nodeB = graph->addNode("Something");
    fdg::Node* nodeC = graph->addNode("Foo");
    fdg::Node* nodeD = graph->addNode("Bar");

    graph->connectNodes(nodeA, nodeB);
    graph->connectNodes(nodeC, nodeD);
    graph->connectNodes(nodeB, nodeD);

    nodeB->setPos(-100.0, -50.0);
    nodeC->setPos(-320.0, 50.0);
    nodeD->setPos(100.0, 50.0);

    graph->show();

    return app.exec();
}
