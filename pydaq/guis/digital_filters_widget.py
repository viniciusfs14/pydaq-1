from ..uis.ui_PYDAQ_Digital_filters_widget import Ui_Digitalfilters_arduino_widget
from PySide6.QtWidgets import QFileDialog, QWidget

class Digital_Filters_Arduino_Widget(QWidget, Ui_Digitalfilters_arduino_widget):
    def __init__(self, *args):
        super(Digital_Filters_Arduino_Widget, self).__init__()
        self.setupUi(self)
        self.filter_combox.currentTextChanged.connect(self.update_filter)
        self.update_filter(self.filter_combox.currentText())
        
    
    # function that show and hide fir or iir widgets    
    def update_filter(self, text):
        if text == 'FIR':
            self.fir_configs.show()
            self.iir_configs.hide()
        else:
            self.iir_configs.show()
            self.fir_configs.hide()