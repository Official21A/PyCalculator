import sys # for handeling the exit status of app

from PyQt5.QtWidgets import QApplication, QLabel, QWidget


app = QApplication(sys.argv)
# instance of qapplication ; with getting a command line "sys.arvg"

window = QWidget() # the base of every component

# use window methods
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80) # for size and location (x, y, wi, he)

helloMsg = QLabel('<h1>Hello World!</h>', parent=window)
helloMsg.move(60, 15) # coordinates of label on app window

window.show() # show the app gui

sys.exit(app.exec_()) # run the app loop
# and to handel what happens after exiting the gui page
