from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFrame, QMessageBox
)
from PySide6.QtCore import Qt

from services.auth_service import login
from session.session_manager import SessionManager
from ui.dashboard_window import DashboardWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ETL Zone - Login")
        self.setFixedSize(450, 300)

        self.build_ui()

    def build_ui(self):
        # ---------- Card ----------
        card = QFrame()
        card.setFixedWidth(380)
        card.setStyleSheet("""
            QFrame {
                background-color: #252526;
                border-radius: 10px;
                padding: 25px;
            }
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(15)

        # ---------- Title ----------
        title = QLabel("Login")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignLeft)

        # ---------- Email ----------
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.email.setFixedHeight(38)

        # ---------- Password ----------
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedHeight(38)

        # ---------- Login Button ----------
        self.login_button = QPushButton("Login")
        self.login_button.setFixedHeight(40)
        self.login_button.clicked.connect(self.handle_login)

        # ---------- Assemble Card ----------
        card_layout.addWidget(title)
        card_layout.addWidget(self.email)
        card_layout.addWidget(self.password)
        card_layout.addWidget(self.login_button)

        # ---------- Center Layout ----------
        root_layout = QVBoxLayout()
        root_layout.addStretch()
        root_layout.addWidget(card, alignment=Qt.AlignCenter)
        root_layout.addStretch()

        self.setLayout(root_layout)

    def handle_login(self):
        email = self.email.text().strip()
        password = self.password.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Validation Error", "Email and password are required")
            return

        self.login_button.setEnabled(False)

        try:
            response = login(email, password)
            print("LOGIN RESPONSE:", response)

            # ✅ FIXED BUG (this caused your crash earlier)
            if response.get("status") == "success":
                SessionManager.set_session(
                    response["token"],
                    response["userCode"],
                    response["role"]
                )

                self.dashboard = DashboardWindow()
                self.dashboard.show()
                self.close()

            else:
                QMessageBox.critical(
                    self,
                    "Login Failed",
                    response.get("msg", "Invalid credentials")
                )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        finally:
            self.login_button.setEnabled(True)
