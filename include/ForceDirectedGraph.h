#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include "Node.h"

class ForceDirectedGraph : public QWidget
{
public:
    ForceDirectedGraph();

    Node* addNode(std::string name);
    void connectNodes(Node* startNode, Node* endNode);
};
