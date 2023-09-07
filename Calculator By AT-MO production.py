import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SimpleCalculator(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('AT-MO Tk: @sinatraGi')
        self.setGeometry(100, 100, 300, 400)
        
        # Set main background to black
        self.setStyleSheet("background-color: black;")

        # Font Styles
        button_font = QFont('Arial', 18)

        # Display with background black and text white
        self.equation_display = QLineEdit(self)
        self.equation_display.setFont(QFont('Arial', 40))
        self.equation_display.setStyleSheet("background-color: black; color: white; border: none;")
        self.equation_display.setReadOnly(True)
        self.equation_display.setAlignment(Qt.AlignRight) 

        # Create Buttons
        buttons = 'C⌫%*789/456+123-0.'
        button_grid = QGridLayout()

        operators = ['%','+', '-', '*', '/', '=']

        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, button_text in zip(positions, buttons):
            btn = QPushButton(button_text)
            btn.setFont(button_font)
            btn.clicked.connect(self.on_button_click)

            if button_text in operators:
                btn.setStyleSheet("QPushButton {"
                                  "border-radius: 30px;"
                                  "background-color: orange;"
                                  "color: white;" 
                                  "}"
                                  "QPushButton:pressed {"
                                  "background-color: #FF4500;"
                                  "}")
            else:
                btn.setStyleSheet("QPushButton {"
                                  "border-radius: 30px;"
                                  "background-color: #2C2C2C;"  
                                  "color: white;"  
                                  "}"
                                  "QPushButton:pressed {"
                                  "background-color: #1E1E1E;"  
                                  "}")

            btn.setFixedSize(60, 60)  
            button_grid.addWidget(btn, *position)

        # Add '=' button with double width (horizontal)
        equal_btn = QPushButton('=')
        equal_btn.setFont(button_font)
        equal_btn.setStyleSheet("QPushButton {"
                                "border-radius: 30px;"
                                "background-color: orange;"
                                "color: white;" 
                                "}"
                                "QPushButton:pressed {"
                                "background-color: #FF4500;"
                                "}")
        equal_btn.setFixedSize(120, 60)
        equal_btn.clicked.connect(self.on_button_click)
        button_grid.addWidget(equal_btn, 4, 2, 1, 2)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.equation_display)
        main_layout.addLayout(button_grid)

        self.setLayout(main_layout)

    def on_button_click(self):
        button_text = self.sender().text()

        if button_text == '=':
            try:
                self.equation_display.setText(str(eval(self.equation_display.text())))
            except:
                self.equation_display.setText("Error")
        elif button_text == 'C':
            self.equation_display.clear()
        elif button_text == '⌫':
            self.equation_display.setText(self.equation_display.text()[:-1])
        else:
            self.equation_display.setText(self.equation_display.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleCalculator()
    window.show()
    sys.exit(app.exec_())
