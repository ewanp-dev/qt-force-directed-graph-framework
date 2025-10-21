#include "ForceDirectedGraph.h"
#include "Edge.h"

#include <QPushButton>
#include <QApplication>
#include <QThread>
#include <QTimer>
#include <QVBoxLayout>
#include <cmath>
#include <unordered_set>
#include <string>
#include <iostream>

ForceDirectedGraph::ForceDirectedGraph(QWidget* parent) 
    : view_(new GraphicsView(this)), scene_(new GraphicsScene())
{
    std::cout << "BUILDING GRAPH" << '\n';
    setContentsMargins(0, 0, 0, 0);

    view_->setScene(scene_);

    QVBoxLayout *mainLayout = new QVBoxLayout();
    mainLayout->setContentsMargins(0, 0, 0, 0);

    mainLayout->addWidget(view_);

    setLayout(mainLayout);

    // std::cout << "SINGLE SHOT METHOD" << '\n';
    // QTimer::singleShot(0, this, &ForceDirectedGraph::initSimulation);
}

void ForceDirectedGraph::initSimulation()
{
    // init timer
    timer_ = new QTimer(this);
    timer_->setTimerType(Qt::PreciseTimer);
    std::cout << "INIT SIMULATION" << '\n';

    std::cout << "AFTER SIMULATION" << '\n';
    const int fps = 60;

    // pause between ticks in milliseconds
    constexpr int interval = static_cast<float>(1000)/60;

    elapsed_.start();
    
    qDebug() << "Starting timer...";
    timer_->start(interval);
    qDebug() << "Event loop running:" << QCoreApplication::instance()->thread()->isRunning();
    qDebug() << "Timer active:" << timer_->isActive();

    bool ok = connect(timer_, &QTimer::timeout, this, &ForceDirectedGraph::tick);
    qDebug() << "connect(tick) =" << ok;

    bool ok2 = connect(timer_, &QTimer::timeout, this, []{
            qDebug() << "[lambda] timeout fired";
            });

    qDebug() << "obj thread =" << QThread::currentThread();
    qDebug() << "app thread =" << qApp->thread();
    qDebug() << "Graph thread = " << this->thread();
    qDebug() << "Event loop running =" << (QCoreApplication::instance()->thread() == QThread::currentThread());

    std::cout << "INIT IS FINISHED" << '\n';
}

Node* ForceDirectedGraph::addNode(std::string name) {
    // placeholder
    Node* node = new Node(name);
    scene_->addItem(node);

    connect(node, &Node::hoverEntered, this, &ForceDirectedGraph::onNodeHoverEnter);
    connect(node, &Node::hoverLeft, this, &ForceDirectedGraph::onNodeHoverLeave);

    nodeStore_.push_back(node);
    return node;
}

void ForceDirectedGraph::connectNodes(Node* startNode, Node* endNode)
{
    scene_->addItem(new Edge(startNode, endNode));
}

void ForceDirectedGraph::connectMultipleNodes(Node* startNode, const std::vector<Node*> &endNodes) {
    for (Node* node : endNodes) {
        scene_->addItem(new Edge(startNode, node));
    } 
}

QPointF ForceDirectedGraph::computeRepulsion(Node *node) 
{
    const double kRepel = 400.0;
    QPointF velocityDelta(0.0, 0.0);

    for (Node* otherNode : nodeStore_) {
        if (node == otherNode) {
            continue;
        }

        QPointF repelDirection = node->pos() - otherNode->pos();
        const float length = sqrt(repelDirection.x()*repelDirection.x() + repelDirection.y()*repelDirection.y());

        repelDirection /= length;
        double magnitude = kRepel / length;

        velocityDelta += repelDirection * magnitude;
    }

    return velocityDelta;
}

QPointF ForceDirectedGraph::computeAttraction(Node *node)
{
    const double kSpring = 0.05;
    const double restLength = 80.0; // distance between nodes

    QPointF velocityDelta(0.0, 0.0);

    for (Edge* edge : node->getConnections()) {
        Node* other = (edge->node == node) ? edge->input : edge->node;
        
        QPointF repelDirection = other->pos() - node->pos();
        const float length = sqrt(repelDirection.x()*repelDirection.x() + repelDirection.y()*repelDirection.y());
        repelDirection /= length;

        double magnitude = kSpring * (length - restLength);
        QPointF springForce = repelDirection * magnitude;

        velocityDelta += springForce;
    }

    return velocityDelta;
}

QPointF ForceDirectedGraph::computeCenterGravity(Node *node)
{
    QPointF center(scene_->sceneRect().center());
    QPointF delta = center - node->pos();
    const double gravity = 0.01;
    return delta * gravity;
}

void ForceDirectedGraph::updatePhysics(double dt) 
{
    std::cout << "STARTING UPDATE PHYSICS" << '\n';
    // TODO: Stop nodes from glitching when moved too far away from nearest input
    // TODO: Stop simulation when node speed gets to a certain threshold
    for (Node* node : nodeStore_) {
        QPointF repulsiveForce = computeRepulsion(node);
        QPointF attractiveForce = computeAttraction(node);
        QPointF gravityForce = computeCenterGravity(node);

        QPointF totalForce = repulsiveForce + attractiveForce + gravityForce;

        node->velocity += totalForce * dt;
        node->velocity *= 0.9;
        if (!node->isDragging()) 
        {
            node->setPos(node->pos() + node->velocity);
        }

        double speed = std::hypot(node->velocity.x(), node->velocity.y());
    }
}

void ForceDirectedGraph::tick() {
    std::cout << "TICK" << '\n';
    const qint64 ns = elapsed_.nsecsElapsed();
    elapsed_.restart();

    // ns to seconds
    double speedMultiplier = 5; // speed up or slow down the graph
    const double dt = ( ns * 1e-9 ) * speedMultiplier;

    updatePhysics(dt);

    // Trigger a redraw
    scene_->update();
}

void ForceDirectedGraph::onNodeHoverEnter(Node *hoveredNode) {
    std::unordered_set<Node*> family = { hoveredNode };
    for (Edge *connection : hoveredNode->getOutputs()) {
        connection->setFadeColor(QColor("#2c2f33"), QColor("#c9bf99"));
        family.insert(connection->node);
    }

    for (Node *node : nodeStore_) {
        if (family.find(node) != family.end()) {
            node->setFadeColor(QColor("#bec4cf"), QColor("#c9bf99"));
        } else {
            node->setFadeColor(QColor("#bec4cf"), QColor("#404040"));
        }
    }
}

void ForceDirectedGraph::onNodeHoverLeave(Node *hoveredNode) {
    for (Edge *connection : hoveredNode->getOutputs()) {
        connection->setFadeColor(QColor("#c9bf99"), QColor("#2c2f33"));
    }

    for (Node *node : nodeStore_) {
        node->setFadeColor(node->brush().color(), QColor("#bec4cf"));
    }
}
