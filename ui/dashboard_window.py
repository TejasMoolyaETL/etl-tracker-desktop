from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QPushButton, QFrame
)
from PySide6.QtCore import Qt

from ui.organization_list import OrganizationList
from session.session_manager import SessionManager


class DashboardWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ETL Zone - Dashboard")
        self.resize(1100, 650)

        self.home_widget = QLabel("Welcome to ETL Zone")
        self.home_widget.setAlignment(Qt.AlignCenter)
        self.home_widget.setStyleSheet(
            "font-size: 20px; color: white;"
        )

        self.build_ui()

    def build_ui(self):
        root = QWidget()
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)

        # ---- Sidebar ----
        sidebar = QFrame()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet("background-color: #1e1e1e;")

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(15, 20, 15, 20)
        sidebar_layout.setSpacing(10)

        title = QLabel("ETL Zone")
        title.setStyleSheet(
            "color: white; font-size: 18px; font-weight: bold;"
        )

        btn_org = QPushButton("Organizations")
        btn_logout = QPushButton("Logout")

        for btn in (btn_org, btn_logout):
            btn.setFixedHeight(38)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #252526;
                    color: #cccccc;
                    border-radius: 8px;
                    text-align: left;
                    padding-left: 12px;
                }
                QPushButton:hover {
                    background-color: #373737;
                    color: white;
                }
            """)

        btn_org.clicked.connect(self.show_organizations)
        btn_logout.clicked.connect(self.logout)

        sidebar_layout.addWidget(title)
        sidebar_layout.addSpacing(20)
        sidebar_layout.addWidget(btn_org)
        sidebar_layout.addStretch()
        sidebar_layout.addWidget(btn_logout)

        # ---- Content ----
        self.content = QFrame()
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.addWidget(self.home_widget)

        root_layout.addWidget(sidebar)
        root_layout.addWidget(self.content)

        self.setCentralWidget(root)

    def show_home(self):
        self.clear_content()
        self.content_layout.addWidget(self.home_widget)

    def show_organizations(self):
        self.clear_content()
        self.content_layout.addWidget(
            OrganizationList(on_back=self.show_home)
        )

    def clear_content(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def logout(self):
        SessionManager.clear()
        self.close()