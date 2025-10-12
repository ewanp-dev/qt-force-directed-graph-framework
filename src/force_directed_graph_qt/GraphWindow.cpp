#include <QApplication>
#include <QPushButton>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    ForceDirectedGraph* graph = new ForceDirectedGraph();

    // Cluster A
    Node* nodeA = graph->addNode("A");
    Node* nodeA1 = graph->addNode("A1");
    Node* nodeA2 = graph->addNode("A2");
    Node* nodeA3 = graph->addNode("A3");

    Node* nodeB = graph->addNode("Something");
    Node* nodeC = graph->addNode("Foo");
    Node* nodeD = graph->addNode("Bar");

    graph->connectNodes(nodeA, nodeB);
    graph->connectNodes(nodeC, nodeD);
    graph->connectNodes(nodeB, nodeD);
    graph->connectMultipleNodes(nodeA, { nodeA1, nodeA2, nodeA3 });

    nodeA1->setPos(200, 50);
    nodeA2->setPos(300, 60);
    nodeA3->setPos(400, 70);
    nodeB->setPos(-100.0, -50.0);
    nodeC->setPos(-320.0, 50.0);
    nodeD->setPos(100.0, 50.0);

    graph->show();

    return app.exec();
}
