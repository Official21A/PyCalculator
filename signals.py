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

# if you need to pass and arg to the func use this
"""
def greeting(who):
    if msg.text():
        msg.setText('')
    else:
        msg.setText(f'Hello {who}')

btn.clicked.connect(functools.partial(greeting, 'World!'))
For this code to work, you need to import functools first.
"""	

layout.addWidget(btn)

msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())