#pragma once

#include <QWidget>
#include <QGraphicsScene>
#include "GraphicsView.h"
#include "GraphicsScene.h"
#include "Node.h"

class ForceDirectedGraph : public QWidget
{
public:
    ForceDirectedGraph();

    Node* addNode(std::string name);

private:
    GraphicsView* view_;
    GraphicsScene* scene_;
};
