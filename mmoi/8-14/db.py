from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType('ui/db.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()