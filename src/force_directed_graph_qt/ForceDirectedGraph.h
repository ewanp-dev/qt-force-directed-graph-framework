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

    private Q_SLOTS:
        void tick();

    private:
        void updatePhysics(double dt);
        QPointF computeRepulsion(Node* node);
        QPointF computeAttraction(Node* node);
        QPointF computeCenterGravity(Node* node);

        QTimer* timer_;
        QElapsedTimer elapsed_;
        std::vector<Node*> nodeStore_;

        GraphicsView* view_;
        GraphicsScene* scene_;

};
