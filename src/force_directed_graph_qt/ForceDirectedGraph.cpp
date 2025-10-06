#include "ForceDirectedGraph.h"

#include <iostream>
#include <QPushButton>
#include <QVBoxLayout>

ForceDirectedGraph::ForceDirectedGraph()
{
    view_ = new QGraphicsView();
    scene_ = new QGraphicsScene();
    view_->setScene(scene_);
    scene_->addRect(0,0,20,20);

    QVBoxLayout* mainLayout = new QVBoxLayout();
    QPushButton* button = new QPushButton ("Hello world !");

    mainLayout->addWidget(button);
    mainLayout->addWidget(view_);

    setLayout(mainLayout);
}

void ForceDirectedGraph::addNode()
{
    std::cout << "creating node\n";
}
