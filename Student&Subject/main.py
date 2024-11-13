from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.MainWindowEx import Ui_MainWindow  # Assuming this is the correct import path
from PyQt6 import uic

app = QApplication([])

# Create main window
main_window = QMainWindow()

# Load the UI
myWindow = Ui_MainWindow()
myWindow.setupUi(main_window)

# Show the main window
main_window.show()

# Execute the application
app.exec()
