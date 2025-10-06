#include "Node.h"
#include <QGraphicsTextItem>
#include <QGraphicsSceneMouseEvent>
#include <GraphicsItemChange>
#include <QPainter>
#include <QCursor>
#include <iostream>
#include <qnamespace.h>

Node::Node(std::string &nodeName, qreal x, qreal y, qreal w, qreal h, QGraphicsItem* parent) : QGraphicsEllipseItem(-w, -h, 2 * w, 2 * h, parent) {
    this->nodeName = nodeName; 
    nodeColor_ = "#bec4cf";
    hoverColor_ = "#c9bf99";
    currentColor_ = nodeColor_;
    charLimit_ = 12;

    this->x = static_cast<float>(x);
    this->y = static_cast<float>(y);
    
    setFlag(GraphicsItemFlag::ItemIsMovable);
    setFlag(GraphicsItemFlag::ItemIsSelectable);
    setFlag(GraphicsItemFlag::ItemSendsGeometryChanges);
    setAcceptHoverEvents(true);
    setPos(x, y);

    label_ = new QGraphicsTextItem(nodeName.c_str());
    label_->setAcceptHoverEvents(true);
    label_->setDefaultTextColor(QColor(nodeColor_.c_str()));
    int yOffset = 4;
    updateLabelPosition_(yOffset);
}

void Node::hoverEnterEvent(QGraphicsSceneHoverEvent *event) {
    currentColor_ = hoverColor_;
    setCursor(Qt::CursorShape::OpenHandCursor);
    updateLabelPosition_(6);
    update();
    QGraphicsEllipseItem::hoverEnterEvent(event);
}

void Node::hoverLeaveEvent(QGraphicsSceneHoverEvent *event) {
    currentColor_ = nodeColor_;
    unsetCursor();
    updateLabelPosition_(4);
    update();
    QGraphicsEllipseItem::hoverLeaveEvent(event);
}

void Node::mousePressEvent(QGraphicsSceneMouseEvent *event) {
    if (event->button() != Qt::MouseButton::LeftButton) {
        QGraphicsEllipseItem::mousePressEvent(event);
    }
}

void Node::mouseReleaseEvent(QGraphicsSceneMouseEvent *event) {
    setSelected(false);
    QGraphicsEllipseItem::mouseReleaseEvent(event);
} 

void Node::paint(QPainter *painter, QStyleOptionGraphicsItem *option, QWidget *widget) {
    painter->setBrush(QBrush(QColor(currentColor_.c_str())));
    // NEEDS FIXING
    painter->setPen(QPen(QColor(currentColor_.c_str()), 2));
    painter->drawEllipse(rect());
}

void Node::itemChange(GraphicsItemChange *change, const QVariant &value) {
    // NEEDS FIXING
    if (change == GraphicsItemChange::ItemPositionHasChanged) {
        setSelected(false);
    }
}

void Node::updateLabelPosition_(int y_pos) {
    QRectF nodeRect = rect();
    QRectF labelRect = label_->boundingRect();

    auto x = nodeRect.center().x() - (labelRect.width() / 2);
    auto y = nodeRect.bottom() + y_pos;
    label_->setPos(x, y);
}

void Node::setName(std::string& name) {
    nodeName = name;
    if (nodeName.length() > this->charLimit_) {
        nodeName = nodeName.substr(0, 12);
    }
    label_->setPlainText(nodeName.c_str());
    updateLabelPosition_(4);
}

QPointF Node::center() {
    return scenePos();
} 



