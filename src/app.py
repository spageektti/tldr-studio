import os
import sys
from PyQt6.QtWidgets import QApplication
from welcome_window import WelcomeWindow

def config_is_valid():
    return True # Placeholder for now

def main():
    if os.path.exists(os.path.expanduser("~/tldr-studio")):
        if(config_is_valid()):
            app = QApplication(sys.argv)
            window = WelcomeWindow()
            window.show()
            sys.exit(app.exec())
        else:
            print("The configuration file is invalid.")
    else:
        print("The folder ~/tldr-studio does not exist.")

if __name__ == "__main__":
    main()