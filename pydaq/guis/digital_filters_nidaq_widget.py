from ..uis.ui_PYDAQ_Digital_filterss_NIDAQ_widget import Ui_Digitalfilters_NIDAQ_widget
from PySide6.QtWidgets import QFileDialog, QWidget
import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, filtfilt, freqz

class Digital_Filters_NIDAQ_Widget(QWidget, Ui_Digitalfilters_NIDAQ_widget):
    def __init__(self, *args):
        super(Digital_Filters_NIDAQ_Widget, self).__init__()
        self.setupUi(self)
        

            
                
    