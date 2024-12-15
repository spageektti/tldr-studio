import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QMenuBar, QMenu
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QAction

class InitWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Please wait... | TLDR Studio")
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1E1E1E;
            }
            QLabel {
                color: #FFFFFF;
                font-family: Inter, sans-serif;
            }
        """)

        self.init_label = self.create_init_label()

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.init_label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.initialize()

    def create_init_label(self):
        init_text = """
        <p style='font-size: 32px; font-weight: semi-bold;'>Initializing TLDR Studio</p>
        <p style='font-size: 16px; color: #EEEEEE; font-weight: 300;'>Please wait while we set things up for you.</p>
        """
        init_label = QLabel(init_text)
        init_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return init_label
    
    def is_command_installed(self, command):
        try:
            subprocess.run([command, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        except FileNotFoundError:
            return False
    
    def initialize(self):
        if os.path.exists(os.path.expanduser("~/tldr-studio")):
            print("tldr-studio exists")
        else:
            print("tldr-studio does not exist")
            os.system("mkdir ~/tldr-studio")
            print("created tldr-studio folder")

        if(self.is_command_installed('tldr-lint')):
            print("tldr-lint is installed")
        else:
            print("tldr-lint is not installed")
            if(self.is_command_installed('npm')):
                print("npm is installed")
                os.system("npm install -g tldr-lint")
            else:
                print("npm is not installed, cannot install tldr-lint")
        
        if(self.is_command_installed('git')):
            print("git is installed")
        else:
            print("git is not installed")
            if(self.is_command_installed('apt')):
                print("apt is installed")
                os.system("sudo apt install -y git")
            elif(self.is_command_installed('dnf')):
                print("dnf is installed")
                os.system("sudo dnf install -y git")
            elif(self.is_command_installed('brew')):
                print("brew is installed")
                os.system("brew install git")
            else:
                print("No package manager found to install git")
        
        if(self.is_command_installed('gh')):
            print("gh is installed")
        else:
            print("gh is not installed")
            # i don't know if there is apt package for gh
            if(self.is_command_installed('dnf')):
                print("dnf is installed")
                os.system("sudo dnf install -y gh")
            elif(self.is_command_installed('brew')):
                print("brew is installed")
                os.system("brew install gh")
            else:
                print("No package manager found to install gh")
        
        if(self.is_command_installed('tldrtranslate')):
            print("tldrtranslate is installed")

        else:
            print("tldrtranslate is not installed")
            os.system("cd ~/tldr-studio && git clone https://github.com/Jaro-c/Argos-API.git")
            os.system("cd ~/tldr-studio/Argos-API && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt")
            print("installed argos-api (tldrtranslate dependency)")
            os.system("pip install argostranslate")
            print("installed argostranslate (tldrtranslate dependency)")
            if(self.is_command_installed('wget')):
                os.system("cd ~/tldr-studio && wget https://github.com/ikks/tldrtranslate/releases/download/v1.0.0/tldrtranslate-x86_64-linux && chmod +x tldrtranslate-x86_64-linux && sudo mv tldrtranslate-x86_64-linux /usr/local/bin/tldrtranslate")
                print("installed tldrtranslate")
            elif(self.is_command_installed('curl')):
                os.system("cd ~/tldr-studio && curl -L https://github.com/ikks/tldrtranslate/releases/download/v1.0.0/tldrtranslate-x86_64-linux -o tldrtranslate-x86_64-linux && chmod +x tldrtranslate-x86_64-linux && mv tldrtranslate-x86_64-linux /usr/local/bin/tldrtranslate")
                print("installed tldrtranslate")
            else:
                print("Neither wget nor curl is installed, cannot install tldrtranslate")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InitWindow()
    window.show()
    sys.exit(app.exec())