from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTableWidget,
    QTableWidgetItem, QFrame
)
from PySide6.QtCore import Qt

from services.organization_service import get_all_organizations


class OrganizationList(QWidget):

    def __init__(self, on_back):
        super().__init__()
        self.on_back = on_back
        self.build_ui()
        self.load_data()

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(30, 30, 30, 30)

        # ---- Card ----
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #2b2b2b;
                border-radius: 12px;
            }
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 24, 24, 24)
        card_layout.setSpacing(16)

        # ---- Header ----
        header = QHBoxLayout()

        title = QLabel("Organizations")
        title.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: 600;
        """)

        btn_back = QPushButton("← Back")
        btn_back.setFixedHeight(36)
        btn_back.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 6px;
                padding: 0 14px;
            }
            QPushButton:hover {
                background-color: #1493ff;
            }
        """)
        btn_back.clicked.connect(self.on_back)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(btn_back)

        # ---- Table ----
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(
            ["Org Code", "Organization Name"]
        )
        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #1e1e1e;
                color: #dddddd;
                gridline-color: #333333;
                border: none;
                font-size: 13px;
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: white;
                padding: 8px;
                border: none;
                font-weight: 600;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #333333;
            }
            QTableWidget::item:selected {
                background-color: #007acc;
                color: white;
            }
        """)

        card_layout.addLayout(header)
        card_layout.addWidget(self.table)

        root.addWidget(card)

    def load_data(self):
        orgs = get_all_organizations()
        self.table.setRowCount(len(orgs))

        for row, org in enumerate(orgs):
            self.table.setItem(row, 0, QTableWidgetItem(org.org_code))
            self.table.setItem(row, 1, QTableWidgetItem(org.org_name))