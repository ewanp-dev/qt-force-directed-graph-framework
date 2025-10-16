#ifndef NODE_H
#define NODE_H
#include <QGraphicsEllipseItem>
#include <QGraphicsView>
#include <QObject>
#include <vector>

class Edge;

class Node : public QObject, public QGraphicsEllipseItem
{
    Q_OBJECT
    public:
        Node(std::string &nodeName, qreal x = 0, qreal y = 0, qreal w = 20.0, qreal h = 20.0, QGraphicsItem* parent = nullptr);
        void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override;
        void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override;
        void mousePressEvent(QGraphicsSceneMouseEvent *event) override;
        void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override;
        QVariant itemChange(GraphicsItemChange change, const QVariant &value) override;
        void setName(std::string& name);
        void setNodeRadius(float radius);
        void addConnection(Edge* connection); // maybe move into private
        void setDefaultColor();
        void setColor(const std::string &color);
        void fadeColor(const QColor &start, const QColor &end, int duration = 150);
        QPointF center();
        float x;
        float y;
        std::string nodeName;
        QPointF velocity;
        std::vector<Edge*> connections;

    Q_SIGNALS:
        void hoverEntered(Node* node);
        void hoverLeft(Node* node);
        
    private:
        void updateLabelPosition_(int y_pos);
        std::string nodeColor_;
        std::string hoverColor_;
        std::string currentColor_;
        int charLimit_;
        QGraphicsTextItem* label_;

};
#endif
