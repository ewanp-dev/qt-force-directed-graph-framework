#include "Edge.h"
#include "Node.h"
#include <QPen>

Edge::Edge(Node* node, Node* input) {
    this->node = node;
    this->input = input;
    this->defaultColor_ = "#2c2f33";
    node->addConnection(this);
    input->addConnection(this);
    setPen(QPen(QColor(defaultColor_.c_str()), 2));
    setZValue(-1.0);
    updatePosition();
}

void Edge::updatePosition() {
    setLine(
        node->center().x(),
        node->center().y(),
        input->center().x(),
        input->center().y()
    );
}

void Edge::setLineColor(std::string color) {
    setPen(QPen(QColor(color.c_str()), 2));
}

void Edge::setDefaultColor() {
    setLineColor(defaultColor_);
}


