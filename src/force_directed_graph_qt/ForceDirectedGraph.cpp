#include "ForceDirectedGraph.h"

#include <QPushButton>
#include <QVBoxLayout>
#include "Edge.h"
#include <QTimer>
#include <QElapsedTimer>
#include <iostream>

ForceDirectedGraph::ForceDirectedGraph() {
    view_ = new GraphicsView();
    scene_ = new GraphicsScene();
    setContentsMargins(0, 0, 0, 0);

    view_->setScene(scene_);

    QVBoxLayout *mainLayout = new QVBoxLayout();
    mainLayout->setContentsMargins(0, 0, 0, 0);

    mainLayout->addWidget(view_);

    setLayout(mainLayout);

    initSimulation();
}

void ForceDirectedGraph::initSimulation()
{
    // init timer
    timer_ = new QTimer(this);
    timer_->setTimerType(Qt::PreciseTimer);
    connect(timer_, &QTimer::timeout, this, &ForceDirectedGraph::tick);

    const int fps = 60;

    // pause between ticks in milliseconds
    constexpr int interval = static_cast<float>(1000)/60;

    elapsed_.start();
    timer_->start(interval);

}

Node* ForceDirectedGraph::addNode(std::string name) {
    // placeholder
    Node* node = new Node(name);
    scene_->addItem(node);
    nodeStore_.push_back(node);
    return node;
}


void ForceDirectedGraph::connectNodes(Node* startNode, Node* endNode)
{
    scene_->addItem(new Edge(startNode, endNode));
}

void ForceDirectedGraph::advanceNode(double dt, Node* node)
{
    // TODO: QPointF may be slow, we should do benchmarking/replace it with a faster vector class

    QPointF velocityDelta;
    for (Node* otherNode : nodeStore_) {
        if(node==otherNode)
        {
            continue;
        }

        QPointF repelDirection = node->pos()-otherNode->pos();
        const float length = sqrt(repelDirection.x()*repelDirection.x() + repelDirection.y()*repelDirection.y());
        repelDirection /= length; // normalize
        velocityDelta += repelDirection;
    }

    QPointF pos = node->pos();
    node->velocity+=velocityDelta*-dt;
    node->setPos(pos+node->velocity);
}

void ForceDirectedGraph::tick() {
    const qint64 ns = elapsed_.nsecsElapsed();
    elapsed_.restart();

    // ns to seconds
    const double dt = ns * 1e-9;
    std::cout << "dt: " << dt << "\n";

    // Update your graph (apply forces, integrate positions)
    for (Node* node : nodeStore_) {
        advanceNode(dt, node);
    }

    // Trigger a redraw
    scene_->update();
}
