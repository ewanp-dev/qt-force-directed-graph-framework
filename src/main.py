import sys

from PyQt6.QtWidgets import QApplication

from window import FDNodeGraphWidget


def main() -> None:
    """
    Main executable of the module
    """
    app = QApplication(sys.argv)
    window = FDNodeGraphWidget()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
