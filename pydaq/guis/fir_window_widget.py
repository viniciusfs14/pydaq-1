from PySide6.QtWidgets import QFileDialog, QWidget
from ..uis.ui_PYDAQ_FIR_widget import Ui_FIR_window

class FirWindow(QWidget, Ui_FIR_window): # Call the FirWindow widget
    def __init__(self):
        super(FirWindow, self).__init__()
        self.setupUi(self)
        self.close_fir_button.clicked.connect(self.close)