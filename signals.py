import sys

from PyQt5.QtWidgets import QApplication, QLabel,QPushButton
from PyQt5.QtWidgets import QVBoxLayout,QWidget 


def greeting():
	# this is a function where the button or any other components connects to
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('Signals and slots')

layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)  # Connect clicked to greeting()
	# so in case of clicking this button by user, it will call the greeting func

layout.addWidget(btn)

msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())