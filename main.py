from PySide6.QtWidgets import QApplication
#from ui.mainwindow import Ui_MainWindow
from pykka import ThreadingActor
from actors.View import View
import sys

app = QApplication(sys.argv)

main_window = View(ThreadingActor.start())
main_window.show()

sys.exit(app.exec())