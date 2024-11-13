import sys

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])

window = QWidget(windowTitle="hello pyqt6")
window.show()
app.exec()
