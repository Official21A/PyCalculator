import sys

from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QToolBar


class Window(QMainWindow): # create a subclass of QMainWindow

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.setWindowTitle('QMainWindow') 
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        # it has to have a centeral element
        self.__createMenu__()
        self.__createToolBar__()
        self.__createStatusBar__()


    def __createMenu__(self):
        # Top menu bar
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)


    def __createToolBar__(self):
        # Top toolbar
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)


    def __createStatusBar__(self):
        # Status bar creation
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())