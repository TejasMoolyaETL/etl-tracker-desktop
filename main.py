import sys
from PySide6.QtWidgets import QApplication
from ui.login_window import LoginWindow

app = QApplication(sys.argv)
with open("styles/app.qss") as f:
    app.setStyleSheet(f.read())

window = LoginWindow()
window.show()

sys.exit(app.exec())
