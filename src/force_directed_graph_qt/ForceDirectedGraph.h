#include <QWidget>
#include <QGraphicsView>
#include <QGraphicsScene>

class ForceDirectedGraph : public QWidget
{
public:
    ForceDirectedGraph();

    void addNode();

private:
    QGraphicsView* view_;
    QGraphicsScene* scene_;
};
