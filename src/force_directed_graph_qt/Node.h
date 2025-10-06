#pragma once
#include <QGraphicsEllipseItem>

class Node : public QGraphicsEllipseItem
{
    public:
        Node(std::string &nodeName, qreal x, qreal y, qreal w, qreal h, QGraphicsItem* parent = nullptr);
        void hoverEnterEvent(QGraphicsSceneHoverEvent *event) override;
        void hoverLeaveEvent(QGraphicsSceneHoverEvent *event) override;
        void mousePressEvent(QGraphicsSceneMouseEvent *event) override;
        void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override;
        void paint(QPainter *painter, QStyleOptionGraphicsItem *option, QWidget *widget);
        void itemChange(GraphicsItemChange *change, const QVariant &value);
        void setName(std::string& name);
        void setPosition(float x, float y);
        void setNodeRadius(float radius);
        QPointF center();
        float x;
        float y;
        std::string nodeName;
        
    private:
        void updateLabelPosition_(int y_pos);
        std::string nodeColor_;
        std::string hoverColor_;
        std::string currentColor_;
        int charLimit_;

        QGraphicsTextItem* label_;

};
