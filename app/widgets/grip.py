from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QSizeGrip


class Grip(QWidget):
    def __init__(self, parent: QWidget, position: Qt.Edge) -> None:
        """
        Initialize the class.
            
        :param parent: The parent widget.
        :param position: The position of the widget
            
        :raise TypeError: If the 'parent' parameter is not a QWidget.
        :raise ValueError: If the 'position' parameter is not of Qt.TopEdge, Qt.BottomEdge, Qt.LeftEdge, or Qt.RightEdge.
        """
        super().__init__(parent=parent)
        self.resize_start_position = None
        self.parent = parent
        self.position = position
        self.size_grip = QSizeGrip(self)
        self.position_mapping = {
            Qt.TopEdge: lambda: self.setGeometry(0, 0, self.parent.width(), 3),
            Qt.BottomEdge: lambda: self.setGeometry(0, self.parent.height() - 3, self.parent.width(), 3),
            Qt.LeftEdge: lambda: self.setGeometry(0, 0, 3, self.parent.height()),
            Qt.RightEdge: lambda: self.setGeometry(self.parent.width() - 3, 0, 3, self.parent.height())
        }
        self.set_grip_position()
        self.set_grip_style()
        self.is_resizing = False

    def set_grip_position(self) -> None:
        """
        Set the position of the grip based on the specified position.
        
        :return: None
        """
        self.position_mapping[self.position]()

    def set_grip_style(self) -> None:
        """
        Set the style of the grip.
        
        :return: None
        """
        self.setStyleSheet("background: transparent;")
        self.size_grip.setStyleSheet("background: rgba(0, 0, 0, 0);")

    def enterEvent(self, event: QMouseEvent) -> None:
        """
        Set the cursor shape based on the position of the grip.

        :param event: The mouse event.
        :type event: QMouseEvent

        :return: None
        """
        if self.position in [Qt.TopEdge, Qt.BottomEdge]:
            self.setCursor(Qt.SizeVerCursor)
        elif self.position in [Qt.LeftEdge, Qt.RightEdge]:
            self.setCursor(Qt.SizeHorCursor)

    def leaveEvent(self, event: QMouseEvent) -> None:
        """
        Handle the leave event.

        :param event: The mouse event.
        :type event: QMouseEvent

        :return: None
        """
        self.unsetCursor()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handle the mouse press event.

        :param event: The mouse event.
        :type event: QMouseEvent

        :return: None
        """
        if event.button() == Qt.LeftButton:
            self._start_resizing(event.globalPos())

    def _start_resizing(self, global_pos: QPoint) -> None:
        """
        Start the resizing process.

        :param global_pos: The global position of the mouse.
        :type global_pos: QPoint

        :return: None
        """
        self.is_resizing = True
        self.resize_start_position = global_pos

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handle the mouse move event.

        :param event: The mouse event.
        :type event: QMouseEvent

        :return: None
        """
        if self.is_resizing:
            cursor_pos: QPoint = event.globalPos()
            delta: QPoint = cursor_pos - self.resize_start_position
            self.resize_start_position = cursor_pos

            if self.position == Qt.RightEdge:
                self._resize_right_edge(cursor_pos, delta)
            elif self.position == Qt.BottomEdge:
                self._resize_bottom_edge(cursor_pos, delta)
            elif self.position == Qt.LeftEdge:
                self._resize_left_edge(cursor_pos, delta)
            elif self.position == Qt.TopEdge:
                self._resize_top_edge(cursor_pos, delta)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """
        Handle the mouse release event.

        :param event: The mouse event.
        :type event: QMouseEvent

        :return: None
        """
        self.is_resizing = False

    def _resize_right_edge(self, cursor: QPoint, delta: QPoint) -> None:
        """
        Resize the right edge of the widget based on the cursor position and delta.

        :param cursor: The current cursor position.
        :type cursor: QPoint
        :param delta: The difference between the current cursor position and the previous cursor position.
        :type delta: QPoint

        :return: None
        """
        min_width = self.parent.minimumWidth()
        new_width = max(min_width, self.parent.width() + delta.x())
        if cursor.x() >= self.parent.x() + min_width:
            self.parent.resize(new_width, self.parent.height())

    def _resize_bottom_edge(self, cursor: QPoint, delta: QPoint) -> None:
        """
        Resize the bottom edge of the widget based on the cursor position and delta.

        :param cursor: The current cursor position.
        :type cursor: QPoint
        :param delta: The difference between the current cursor position and the previous cursor position.
        :type delta: QPoint

        :return: None
        """
        min_height = self.parent.minimumHeight()
        new_height = max(min_height, self.parent.height() + delta.y())
        if cursor.y() >= self.parent.y() + min_height:
            self.parent.resize(self.parent.width(), new_height)

    def _resize_left_edge(self, cursor: QPoint, delta: QPoint) -> None:
        """
        Resize the left edge of the widget based on the cursor position and delta.

        :param cursor: The current cursor position.
        :type cursor: QPoint
        :param delta: The difference between the current cursor position and the previous cursor position.
        :type delta: QPoint

        :return: None
        """
        min_width = self.parent.minimumWidth()
        new_width = max(min_width, self.parent.width() - delta.x())
        new_x = self.parent.x() + delta.x()
        if cursor.x() <= self.parent.x() + self.parent.width() - min_width:
            self.parent.setGeometry(new_x, self.parent.y(), new_width, self.parent.height())

    def _resize_top_edge(self, cursor: QPoint, delta: QPoint) -> None:
        """
        Resize the top edge of the widget based on the cursor position and delta.

        :param cursor: The current cursor position.
        :type cursor: QPoint
        :param delta: The difference between the current cursor position and the previous cursor position.
        :type delta: QPoint

        :return: None
        """
        min_height = self.parent.minimumHeight()
        new_height = max(min_height, self.parent.height() - delta.y())
        new_y = self.parent.y() + delta.y()
        if cursor.y() <= self.parent.y() + self.parent.height() - min_height:
            self.parent.setGeometry(self.parent.x(), new_y, self.parent.width(), new_height)
