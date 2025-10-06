#pragma once

#include <QWidget>
#include "GraphicsView.h"
#include "GraphicsScene.h"
#include <QGraphicsScene>

class ForceDirectedGraph : public QWidget
{
public:
    ForceDirectedGraph();

    void addNode();

private:
    GraphicsView* view_;
    QGraphicsScene* scene_;
};
