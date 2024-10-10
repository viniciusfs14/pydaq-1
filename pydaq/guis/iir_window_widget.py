from PySide6.QtWidgets import QFileDialog, QWidget
from ..uis.ui_PYDAQ_IIR_widget import Ui_IIR_window

class IrrWindow(QWidget, Ui_IIR_window): # Call the Iir window widget
    def __init__(self):
        super(IrrWindow, self).__init__()
        self.setupUi(self)
        self.close_iir_button.clicked.connect(self.close)
        