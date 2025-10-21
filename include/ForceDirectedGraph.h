#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include <QElapsedTimer>
#include <vector>
#include "Node.h"

class ForceDirectedGraph : public QWidget
{
    Q_OBJECT
    public:
        ForceDirectedGraph(QWidget* parent = nullptr);

        Node* addNode(std::string name);
        void connectNodes(Node* startNode, Node* endNode);
        void connectMultipleNodes(Node* startNode, const std::vector<Node*>& endNodes);

        void initSimulation();

    protected:
        void onNodeHoverEnter(Node* hoveredNode);
        void onNodeHoverLeave(Node* hoveredNode);
};
