#include "ForceDirectedGraph.h"

#include <QPushButton>
#include <QVBoxLayout>
#include "Edge.h"

ForceDirectedGraph::ForceDirectedGraph() {
    view_ = new GraphicsView();
    scene_ = new GraphicsScene();
    setContentsMargins(0, 0, 0, 0);

    view_->setScene(scene_);

    QVBoxLayout *mainLayout = new QVBoxLayout();
    mainLayout->setContentsMargins(0, 0, 0, 0);

    mainLayout->addWidget(view_);

    setLayout(mainLayout);
}

Node* ForceDirectedGraph::addNode(std::string name) {
    // placeholder
    Node* node = new Node(name);
    scene_->addItem(node);
    return node;
}

void ForceDirectedGraph::connectNodes(Node* startNode, Node* endNode)
{
    scene_->addItem(new Edge(startNode, endNode));
}
