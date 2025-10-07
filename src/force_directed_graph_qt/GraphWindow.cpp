#include <QApplication>
#include <QPushButton>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    ForceDirectedGraph* graph = new ForceDirectedGraph();
    Node* node_a = graph->addNode("Hello World");
    Node* node_b = graph->addNode("Something");
    node_b->setPos(-100.0, -50.0);

    graph->show();

    return app.exec();
}
