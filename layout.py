import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QWidget


app = QApplication(sys.argv) # an instance of our gui app

window = QWidget() # create a window

window.setWindowTitle('QHBoxLayout')

"""
# QHBox
layout = QHBoxLayout() # creating a layout
# adding components
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))

"""
"""
# QVBox
layout = QVBoxLayout()

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Bottom'))

"""
"""
# QGrid
layout = QGridLayout()

layout.addWidget(QPushButton('Button (0, 0)'), 0, 0) # (Comp, x, y, hsp, vsp)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)

"""
"""
# QForm
layout = QFormLayout()

layout.addRow('Name:', QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job:', QLineEdit())
layout.addRow('Hobbies:', QLineEdit())

"""

window.setLayout(layout) # setting the layout

window.show()
sys.exit(app.exec_())