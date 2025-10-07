#include <QApplication>
#include <QPushButton>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);


    ForceDirectedGraph* graph = new ForceDirectedGraph();

    graph->resize(1200,800);

    Node* nodeA = graph->addNode("Hello World");
    Node* nodeB = graph->addNode("Something");
    Node* nodeC = graph->addNode("Foo");
    Node* nodeD = graph->addNode("Bar");

    graph->connectNodes(nodeA, nodeB);
    graph->connectNodes(nodeC, nodeD);
    graph->connectNodes(nodeB, nodeD);

    nodeB->setPos(-100.0, -50.0);
    nodeC->setPos(-320.0, 50.0);
    nodeD->setPos(100.0, 50.0);

    graph->show();

    return app.exec();
}
