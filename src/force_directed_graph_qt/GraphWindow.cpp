#include <QApplication>
#include <QPushButton>
#include <iostream>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    ForceDirectedGraph* graph = new ForceDirectedGraph();
    graph->resize(1200,800);

    Node* nodeA = graph->addNode("A");
    Node* nodeA1 = graph->addNode("A1");
    Node* nodeA2 = graph->addNode("A2");
    Node* nodeA3 = graph->addNode("A3");
    Node* nodeB = graph->addNode("B");
    Node* nodeC = graph->addNode("C");
    Node* nodeD = graph->addNode("D");

    graph->connectNodes(nodeA, nodeB);
    graph->connectMultipleNodes(nodeA, { nodeA1, nodeA2, nodeA3 });
    graph->connectNodes(nodeC, nodeD);
    graph->connectNodes(nodeB, nodeD);

    nodeA1->setPos(100, 0);
    nodeA2->setPos(100, -25);
    nodeA3->setPos(100, -50);
    nodeB->setPos(-100.0, -50.0);
    nodeC->setPos(-320.0, 50.0);
    nodeD->setPos(100.0, 50.0);

    // NOTE: Right now clusters are too far apart
    // new cluster
    Node* nodeE = graph->addNode("E");
    Node* nodeE1 = graph->addNode("E1");
    Node* nodeE2 = graph->addNode("E2");
    Node* nodeE3 = graph->addNode("E3");
    Node* nodeE4 = graph->addNode("E4");

    graph->connectMultipleNodes(nodeE, { nodeE1, nodeE2, nodeE3, nodeE4 });

    nodeE->setPos(0, 100);
    nodeE1->setPos(-50, 125);
    nodeE2->setPos(-25, 125);
    nodeE3->setPos(0, 120);
    nodeE4->setPos(20, 100);


    graph->show();

    return app.exec();
}
