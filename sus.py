from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QDialog

class NewWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Window")
        self.layout = QVBoxLayout()

        self.no_button = QPushButton("No", self)
        self.layout.addWidget(self.no_button)

        self.setLayout(self.layout)

        # Conectar o botão 'Não' ao método de retorno
        self.no_button.clicked.connect(self.return_no)

    def return_no(self):
        # Chamar o método para marcar 'Não' no rádio original
        self.parent().select_no()
        self.close()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.layout = QVBoxLayout()

        self.radio_yes = QRadioButton("Yes")
        self.radio_no = QRadioButton("No")

        self.layout.addWidget(self.radio_yes)
        self.layout.addWidget(self.radio_no)

        self.radio_yes.toggled.connect(self.open_new_window)

        self.setLayout(self.layout)

    def open_new_window(self):
        if self.radio_yes.isChecked():
            self.new_window = NewWindow(self)
            self.new_window.show()

    def select_no(self):
        # Marcar o rádio 'Não' da janela principal
        self.radio_no.setChecked(True)

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
