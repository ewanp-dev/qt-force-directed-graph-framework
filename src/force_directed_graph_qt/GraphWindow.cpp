#include <QApplication>
#include <QPushButton>

#include "ForceDirectedGraph.h"

int main(int argc, char **argv)
{
    QApplication app (argc, argv);

    ForceDirectedGraph* graph = new ForceDirectedGraph();
    graph->show();

    return app.exec();
}
