#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include <QElapsedTimer>
#include <vector>
#include "Node.h"

class ForceDirectedGraph : public QWidget
{
    public:
        ForceDirectedGraph(QWidget* parent = nullptr);

        Node* addNode(std::string name);
        void connectNodes(Node* startNode, Node* endNode);
        void connectMultipleNodes(Node* startNode, const std::vector<Node*>& endNodes);

    protected:
        void onNodeHoverEnter(Node* hoveredNode);
        void onNodeHoverLeave(Node* hoveredNode);
};
