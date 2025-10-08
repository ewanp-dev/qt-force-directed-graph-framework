#ifndef EDGE_H
#define EDGE_H

#include <QGraphicsLineItem>

class Node;

class Edge : public QGraphicsLineItem
{
    public:
        Edge(Node* node, Node* input);
        Node* node;
        Node* input;
        void updatePosition();
        void setLineColor(std::string color);
        void setDefaultColor();
};

#endif
