#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include <QElapsedTimer>
#include "GraphicsView.h"
#include "GraphicsScene.h"
#include "Node.h"

class ForceDirectedGraph : public QWidget
{
public:
    ForceDirectedGraph();

    Node* addNode(std::string name);
    void connectNodes(Node* startNode, Node* endNode);

private:
    void tick();
    void initSimulation();
    void advanceNode(double dt, Node* node);

    QTimer* timer_;
    QElapsedTimer elapsed_;
    double accumulator_ = 0.0;
    const double step_ = 1.0 / 120.0; // 120 Hz physics step

    GraphicsView* view_;
    GraphicsScene* scene_;

    std::vector<Node*> nodeStore_;
};
