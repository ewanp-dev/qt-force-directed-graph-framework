import sys

from PyQt6.QtWidgets import QApplication

from window import ForceDrivenNodeEditorWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    wnd = ForceDrivenNodeEditorWindow()
    sys.exit(app.exec())
