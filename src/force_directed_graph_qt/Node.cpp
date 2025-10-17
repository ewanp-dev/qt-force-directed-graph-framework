#include "Node.h"
#include "Edge.h"
#include <QGraphicsTextItem>
#include <QGraphicsSceneMouseEvent>
#include <QVariantAnimation>
#include <QPainter>
#include <QCursor>
#include <qnamespace.h>

Node::Node(std::string &nodeName, qreal x, qreal y, qreal w, qreal h, QGraphicsItem* parent) 
: QGraphicsEllipseItem(-w, -h, 2 * w, 2 * h, parent) 
{
    nodeName_ = nodeName; 
    x_ = static_cast<float>(x);
    y_ = static_cast<float>(y);
    nodeColor_ = "#bec4cf";
    hoverColor_ = "#c9bf99";
    charLimit_ = 12;

    setFlag(GraphicsItemFlag::ItemIsMovable);
    setFlag(GraphicsItemFlag::ItemIsSelectable);
    setFlag(GraphicsItemFlag::ItemSendsGeometryChanges);
    setAcceptHoverEvents(true);
    setPen(Qt::NoPen);
    setPos(x_, y_);
    setColor(nodeColor_);

    label_ = new QGraphicsTextItem(nodeName_.c_str(), this);
    label_->setAcceptHoverEvents(false);
    label_->setDefaultTextColor(QColor(nodeColor_.c_str()));

    int yOffset = 4;
    updateLabelPosition_(yOffset);
}

void Node::hoverEnterEvent(QGraphicsSceneHoverEvent *event) {
    hoverEntered(this);
    setColor(hoverColor_);
    setCursor(Qt::CursorShape::OpenHandCursor);
    updateLabelPosition_(6);
    update();
    QGraphicsEllipseItem::hoverEnterEvent(event);
}

void Node::hoverLeaveEvent(QGraphicsSceneHoverEvent *event) {
    hoverLeft(this);
    setDefaultColor();
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

QVariant Node::itemChange(GraphicsItemChange change, const QVariant &value) {
    if (change == GraphicsItemChange::ItemPositionHasChanged) {
        setSelected(false);
        for (Edge* conn : connections) {
            conn->updatePosition();
        }
    }
    return QGraphicsEllipseItem::itemChange(change, value);
}

void Node::updateLabelPosition_(int y_pos) {
    QRectF nodeRect = rect();
    QRectF labelRect = label_->boundingRect();

    auto x = nodeRect.center().x() - (labelRect.width() / 2);
    auto y = nodeRect.bottom() + y_pos;
    label_->setPos(x, y);
}

void Node::setName(std::string& name) {
    nodeName_ = name;
    if (nodeName_.length() > this->charLimit_) {
        nodeName_ = nodeName_.substr(0, 12);
    }
    label_->setPlainText(nodeName_.c_str());
    updateLabelPosition_(4);
}

std::string Node::nodeName() {
    return nodeName_;
}

void Node::setNodeRadius(float radius) {
    if (radius < 0.001) {
        radius = 0.001;
    } else if (radius > 150) {
        radius = 150;
    }

    setRect(-radius / 2, -radius / 2, radius, radius);
}

void Node::addConnection(Edge* connection) {
    connections.push_back(connection);
}

QPointF Node::center() {
    return scenePos();
} 

void Node::setColor(const std::string &color) {
    QColor qcolor(color.c_str());
    setBrush(QBrush(qcolor));
    update();
}

void Node::fadeColor(const QColor &start, const QColor &end, int duration) {
    // TODO: This is not the fastest way of going about this right now, integrate with QTimer at some point
    auto *anim = new QVariantAnimation(this);
    anim->setDuration(duration);
    anim->setStartValue(start);
    anim->setEndValue(end);

    connect(anim, &QVariantAnimation::valueChanged, this, [this](const QVariant &value) {
        QColor c = value.value<QColor>();
        this->setBrush(QBrush(c));
        if (label_) {
            label_->setDefaultTextColor(c);
        }
        this->update();
    });

    anim->start(QAbstractAnimation::DeleteWhenStopped);
}

void Node::setDefaultColor() {
    QColor qcolor(nodeColor_.c_str());
    setBrush(QBrush(qcolor));
}


