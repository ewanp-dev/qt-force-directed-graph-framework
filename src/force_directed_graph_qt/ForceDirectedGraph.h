#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include <QElapsedTimer>
#include <vector>
#include "GraphicsView.h"
#include "GraphicsScene.h"
#include "Node.h"

class ForceDirectedGraph : public QWidget
{
    public:
        ForceDirectedGraph(QWidget *parent = nullptr);

        Node* addNode(std::string name);
        void connectNodes(Node *startNode, Node *endNode);
        void connectMultipleNodes(Node *startNode, std::vector<Node*> endNodes);

    private:
        void tick();
        void initSimulation();
        void updatePhysics(double dt);
        QPointF computeRepulsion(Node *node);
        QPointF computeAttraction(Node *node);
        QPointF computeCenterGravity(Node *node);
        void onNodeHoverEnter(Node *hoveredNode);
        void onNodeHoverLeave(Node *hoveredNode);

        QTimer* timer_;
        QElapsedTimer elapsed_;
        double accumulator_ = 0.0;
        std::vector<Node*> nodeStore_;
        const double step_ = 1.0 / 120.0;

        GraphicsView* view_;
        GraphicsScene* scene_;

};
