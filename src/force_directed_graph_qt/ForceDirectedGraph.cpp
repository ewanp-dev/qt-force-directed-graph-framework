#include "ForceDirectedGraph.h"

#include <QPushButton>
#include <QVBoxLayout>
#include <iostream>

ForceDirectedGraph::ForceDirectedGraph() {
  view_ = new GraphicsView();
  scene_ = new GraphicsScene();

  view_->setScene(scene_);
  scene_->addRect(-100, -100, 20, 20, QPen("red"));

  QVBoxLayout *mainLayout = new QVBoxLayout();
  QPushButton *button = new QPushButton("Hello world !");

  mainLayout->addWidget(button);
  mainLayout->addWidget(view_);

  setLayout(mainLayout);
}

void ForceDirectedGraph::addNode() {
  // placeholder
  std::cout << "creating node\n";
}
