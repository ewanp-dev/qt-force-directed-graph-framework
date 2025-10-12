#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include <vector>
#include "GraphicsView.h"
#include "GraphicsScene.h"
#include "Node.h"

class ForceDirectedGraph : public QWidget
{
public:
    ForceDirectedGraph();

    Node* addNode(std::string name);
    void connectNodes(Node* startNode, Node* endNode);
    void connectMultipleNodes(Node* startNode, std::vector<Node*> endNodes);

private:
    GraphicsView* view_;
    GraphicsScene* scene_;
};
