#pragma once

#include <QGraphicsEllipseItem>
#include <QGraphicsView>
#include <QObject>
#include <vector>

class Edge;

class Node : public QObject, public QGraphicsEllipseItem
{
    Q_OBJECT
    Q_SIGNALS:
        void hoverEntered(Node* node);
        void hoverLeft(Node* node);

    public:
        Node(std::string &nodeName, qreal x = 0, qreal y = 0, qreal w = 20.0, 
             qreal h = 20.0, QGraphicsItem* parent = nullptr);

        void setName(std::string& name);
        void setNodeRadius(float radius);
        void addConnection(Edge* connection);
        void setDefaultColor();
        void setColor(const std::string &color);
        void fadeColor(const QColor &start, const QColor &end, int duration = 150);
        std::string nodeName();
        QPointF center();

        std::vector<Edge*> connections;
        QPointF velocity;

    protected:
        void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override;
        void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override;
        void mousePressEvent(QGraphicsSceneMouseEvent *event) override;
        void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override;
        QVariant itemChange(GraphicsItemChange change, const QVariant &value) override;

    private:
        void updateLabelPosition_(int y_pos);

        std::string nodeName_;
        std::string nodeColor_;
        std::string hoverColor_;
        int charLimit_, x_, y_;
        QGraphicsTextItem* label_;
};
