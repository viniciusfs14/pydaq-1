from PySide6.QtWidgets import QDialog

from ..uis.ui_warning_digital_filters_window import Ui_Dialog_rt_filter


class Warning_window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_rt_filter()
        self.ui.setupUi(self)

        self.ui.yes_warning.released.connect(self.yes)
        self.ui.no_warning.released.connect(self.no)
        

    def yes(self):
        self.close()
        
    def no(self):
        if self.parent():
            self.parent().select_no()
        self.close()
