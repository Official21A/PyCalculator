import sys

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget 


__version__ = '0.1'
__author__ = 'Amirhossein'


class PyCalcUi(QMainWindow): # the main window class
    def __init__(self):
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)


def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()