from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor, QFont, QConicalGradient
from PySide6.QtWidgets import QWidget

class CPBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.p = 0
        self.setMinimumSize(240, 240)

    def upd(self, pp):
        if self.p == pp:
            return
        self.p = pp
        self.update()

    def resizeEvent(self, event):
        side = min(self.width(), self.height())
        self.setFixedSize(side, side)
        super().resizeEvent(event)

    def paintEvent(self, e):
        pd = self.p * 360
        rd = 360 - pd
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.translate(4, 4)
        
        path, path2 = QPainterPath(), QPainterPath()
        circle_width = self.width() - self.width() / 10
        width_half = circle_width / 2
        circle_rect = QRectF(self.rect().left() / 2, self.rect().top() / 2, circle_width, self.height() - self.height() / 10)

        # Create a gradient for the progress arc
        gradient = QConicalGradient(circle_rect.center(), 90)
        gradient.setColorAt(0.0, QColor("#30b7e0"))
        gradient.setColorAt(1.0, QColor("#a0e0f0"))

        pen, pen2 = QPen(), QPen()
        pen.setCapStyle(Qt.FlatCap)
        pen.setBrush(gradient)
        pen_width = self.width() / 25
        pen.setWidth(pen_width)
        
        path.moveTo(width_half, 0)
        path.arcTo(circle_rect, 90, -pd)
        p.strokePath(path, pen)

        pen2.setWidth(pen_width)
        pen2.setColor(QColor("#d7d7d7"))
        pen2.setCapStyle(Qt.FlatCap)
        pen2.setDashPattern([0.5, 1.105])
        pen2.setDashOffset(2.2)
        
        path2.moveTo(width_half, 0)
        path2.arcTo(circle_rect, 90, rd)
        p.strokePath(path2, pen2)

        # Draw the percentage text in the center
        font = QFont()
        percent_size = self.height() / 7
        font.setPointSizeF(percent_size)
        p.setFont(font)
        p_in_percent = round(self.p * 100, 0)
        
        percent_text_position = self.rect().center()
        percent_text_position.setX(percent_text_position.x() - (
                percent_size + (self.width()/6 if p_in_percent >= 100 else self.width()/10 if p_in_percent >= 10 else self.width()/40)))
        percent_text_position.setY(percent_text_position.y() + percent_size * 2 / 5)
        
        p.setPen(QPen(QColor("#ffffff")))
        p.drawText(percent_text_position, f"{p_in_percent}%")