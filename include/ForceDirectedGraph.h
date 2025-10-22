#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include <QElapsedTimer>
#include <vector>
#include "Node.h"

namespace fdg
{

class ForceDirectedGraph : public QWidget
{
    public:
        ForceDirectedGraph(QWidget* parent = nullptr);

        fdg::Node* addNode(std::string name);
        void connectNodes(fdg::Node* startNode, fdg::Node* endNode);
        void connectMultipleNodes(fdg::Node* startNode, const std::vector<fdg::Node*>& endNodes);

    protected:
        void onNodeHoverEnter(fdg::Node* hoveredNode);
        void onNodeHoverLeave(fdg::Node* hoveredNode);
};

}

