#pragma once

#include <QGraphicsLineItem>
#include <QObject>

class Node;

class Edge : public QObject, public QGraphicsLineItem
{
    Q_OBJECT
    public:
        Edge(Node* node, Node* input);
        Node* node;
        Node* input;
        void updatePosition();
        void setLineColor(std::string color);
        void setDefaultColor();
        void setFadeColor(const QColor &start, const QColor &end, int duration = 150);
};
