import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QMenuBar, QMenu
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QAction

class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to TLDR Studio")
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1E1E1E;
            }
            QLabel {
                color: #FFFFFF;
                font-family: Inter, sans-serif;
            }
            QPushButton {
                background-color: #2B2D30;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #3A3D40;
            }
            QPushButton:pressed {
                background-color: #1F2123;
            }
        """)

        self.create_menu_bar()

        self.welcome_label = self.create_welcome_label()
        self.buttons = self.create_buttons()

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.buttons)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        settings_menu = QMenu("Settings", self)
        menu_bar.addMenu(settings_menu)

    def create_welcome_label(self):
        welcome_text = """
        <p style='font-size: 32px; font-weight: semi-bold;'>Welcome to TLDR Studio</p>
        <p style='font-size: 16px; color: #EEEEEE; font-weight: 300;'><span style='font-weight: 500;'>Create</span> a new TLDR page to share concise information.</p>
        <p style='font-size: 16px; color: #EEEEEE; font-weight: 300;'><span style='font-weight: 500;'>Edit</span> an existing page to refine its content and improve clarity.</p>
        <p style='font-size: 16px; color: #EEEEEE; font-weight: 300;'><span style='font-weight: 500;'>Translate</span> a page to a different language to reach a wider audience.</p>
    """
        welcome_label = QLabel(welcome_text)
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return welcome_label

    def create_buttons(self):
        create_button = self.create_button("icons/create.png", "Create")
        edit_button = self.create_button("icons/edit.png", "Edit")
        translate_button = self.create_button("icons/translate.png", "Translate")

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)

        for button, label in [(create_button, "Create"), (edit_button, "Edit"), (translate_button, "Translate")]:
            button_layout = QVBoxLayout()
            button_layout.setSpacing(10)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
            button_layout.addWidget(QLabel(f"<p style='font-size: 18px; font-weight: 500;'>{label}</p>"), alignment=Qt.AlignmentFlag.AlignCenter)
            buttons_layout.addLayout(button_layout)

        buttons = QWidget()
        buttons.setLayout(buttons_layout)
        return buttons

    def create_button(self, icon_path, label):
        button = QPushButton()
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(48, 48))
        button.setFixedSize(68, 68)
        return button

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_layout()

    def update_layout(self):
        target_width = 1920
        target_height = 1080
        current_width = self.width()
        current_height = self.height()

        width_scale = current_width / target_width
        height_scale = current_height / target_height

        min_margin = 20
        margin_x = max(int(100 * width_scale), min_margin)
        margin_y = max(int(100 * height_scale), min_margin)

        for layout in self.buttons.findChildren(QVBoxLayout):
            layout.setContentsMargins(margin_x, margin_y, margin_x, margin_y)

        main_layout = self.centralWidget().layout()
        main_layout.setContentsMargins(int(200 * width_scale), int(200 * height_scale), int(200 * width_scale), int(200 * height_scale))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec())
