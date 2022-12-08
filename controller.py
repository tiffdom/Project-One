from PyQt5.QtWidgets import *
from view import *
import shapes.area as a  # imports file containing area formula
import shapes.perimeter as p  # imports file containing perimeter formula

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_submit.clicked.connect(lambda: self.submit())
        self.radioButton_circle.clicked.connect(lambda: self.circle())
        self.radioButton_square.clicked.connect(lambda: self.square())
        self.radioButton_rectangle.clicked.connect(lambda: self.rectangle())
        self.radioButton_triangle.clicked.connect(lambda: self.triangle())

    '''
    This function is for the clear button.
    When called, it clears everything from the input boxes.
    All labels and input boxes are enabled.
    '''

    def clear(self):
        self.label_radius.setEnabled(True)
        self.label_side1.setEnabled(True)
        self.label_side2.setEnabled(True)
        self.label_side3.setEnabled(True)
        self.input_radius.setEnabled(True)
        self.input_side1.setEnabled(True)
        self.input_side2.setEnabled(True)
        self.input_side3.setEnabled(True)

        self.radioButton_area.setChecked(True)
        self.radioButton_circle.setChecked(True)

        self.input_radius.setText('')
        self.input_side1.setText('')
        self.input_side2.setText('')
        self.input_side3.setText('')
        self.label_output.setText('Please select calculation and shape.\n'
                                  'Then enter in values and submit.\n'
                                  'Press clear to reset.')

    '''
    This function is for the circle radio button.
    When called, user can only enter in a value for radius.
    Other labels and input boxes are disabled.
    '''

    def circle(self):
        self.label_radius.setEnabled(True)
        self.label_side1.setEnabled(False)
        self.label_side2.setEnabled(False)
        self.label_side3.setEnabled(False)
        self.input_radius.setEnabled(True)
        self.input_side1.setEnabled(False)
        self.input_side2.setEnabled(False)
        self.input_side3.setEnabled(False)

    '''
    This function is for the square radio button.
    When called, user can only enter in a value for side 1.
    Other labels and input boxes are disabled.
    '''

    def square(self):
        self.label_radius.setEnabled(False)
        self.label_side1.setEnabled(True)
        self.label_side2.setEnabled(False)
        self.label_side3.setEnabled(False)
        self.input_radius.setEnabled(False)
        self.input_side1.setEnabled(True)
        self.input_side2.setEnabled(False)
        self.input_side3.setEnabled(False)

    '''
    This function is for the rectangle radio button.
    When called, user can only enter in values for side 1 and side 2.
    Other labels and input boxes are disabled.
    '''

    def rectangle(self):
        self.label_radius.setEnabled(False)
        self.label_side1.setEnabled(True)
        self.label_side2.setEnabled(True)
        self.label_side3.setEnabled(False)
        self.input_radius.setEnabled(False)
        self.input_side1.setEnabled(True)
        self.input_side2.setEnabled(True)
        self.input_side3.setEnabled(False)

    '''
    This function is for the triangle radio button.
    When called, side 1 and side 2 are enabled if area radio button is selected.
    If perimeter radio button is selected, side 1, 2, and 3 are enabled.
    Other labels and input boxes are disabled. 
    '''

    def triangle(self):
        if self.radioButton_area.isChecked():
            self.label_radius.setEnabled(False)
            self.label_side1.setEnabled(True)
            self.label_side2.setEnabled(True)
            self.label_side3.setEnabled(False)
            self.input_radius.setEnabled(False)
            self.input_side1.setEnabled(True)
            self.input_side2.setEnabled(True)
            self.input_side3.setEnabled(False)

        elif self.radioButton_perimeter.isChecked():
            self.label_radius.setEnabled(False)
            self.label_side1.setEnabled(True)
            self.label_side2.setEnabled(True)
            self.label_side3.setEnabled(True)
            self.input_radius.setEnabled(False)
            self.input_side1.setEnabled(True)
            self.input_side2.setEnabled(True)
            self.input_side3.setEnabled(True)

    '''
    This function is for the submit button.
    It uses exception handling to tell the user what went wrong.
    If else statements are used to take in account which radio button has been selected.
    The calculation and answer is displayed for the user to read.
    Finally, all labels and input boxes are enabled for the next calculation.
    '''

    def submit(self):
        try:
            if self.radioButton_area.isChecked():
                if self.radioButton_circle.isChecked():
                    radius = float(self.input_radius.text())
                    if radius < 0:
                        raise Exception
                    area = a.circle(radius)
                    self.label_output.setText(f'Area of circle is radius x pi\n'
                                              f'{radius} x pi = {area}\n'
                                              f'Area = {area}')
                elif self.radioButton_square.isChecked():
                    side1 = float(self.input_side1.text())
                    if side1 < 0:
                        raise Exception
                    area = a.square(side1)
                    self.label_output.setText(f'Area of square is length x width\n'
                                              f'{side1} x {side1} = {area}\n'
                                              f'Area = {area}')
                elif self.radioButton_rectangle.isChecked():
                    side1 = float(self.input_side1.text())
                    side2 = float(self.input_side2.text())
                    if (side1 < 0) or (side2 < 0):
                        raise Exception
                    area = a.rectangle(side1, side2)
                    self.label_output.setText(f'Area of rectangle is length x width\n'
                                              f'{side1} x {side2} = {area}\n'
                                              f'Area = {area}')
                elif self.radioButton_triangle.isChecked():
                    side1 = float(self.input_side1.text())
                    side2 = float(self.input_side2.text())
                    if (side1 < 0) or (side2 < 0):
                        raise Exception
                    area = a.triangle(side1, side2)
                    self.label_output.setText(f'Area of triangle is base x height x 0.5\n'
                                              f'{side1} x {side2} x 0.5 = {area}\n'
                                              f'Area = {area}')
                else:
                    self.label_output.setText('Please select shape.')
            elif self.radioButton_perimeter.isChecked():
                if self.radioButton_circle.isChecked():
                    radius = float(self.input_radius.text())
                    if radius < 0:
                        raise Exception
                    perimeter = p.circle(radius)
                    self.label_output.setText(f'Perimeter of circle is 2 x pi x radius\n'
                                              f'2 x pi x {radius} = {perimeter}\n'
                                              f'Perimeter = {perimeter}')
                elif self.radioButton_square.isChecked():
                    side1 = float(self.input_side1.text())
                    if side1 < 0:
                        raise Exception
                    perimeter = p.square(side1)
                    self.label_output.setText(f'Perimeter of square is length x 4\n'
                                              f'{side1} x 4 = {perimeter}\n'
                                              f'Perimeter = {perimeter}')
                elif self.radioButton_rectangle.isChecked():
                    side1 = float(self.input_side1.text())
                    side2 = float(self.input_side2.text())
                    if (side1 < 0) or (side2 < 0):
                        raise Exception
                    perimeter = p.rectangle(side1, side2)
                    self.label_output.setText(f'Perimeter of rectangle is 2(length + width)\n'
                                              f' 2 x ({side1} + {side2}) = {perimeter}\n'
                                              f'Perimeter = {perimeter}')
                elif self.radioButton_triangle.isChecked():
                    side1 = float(self.input_side1.text())
                    side2 = float(self.input_side2.text())
                    side3 = float(self.input_side3.text())
                    if (side1 < 0) or (side2 < 0) or (side3 < 0):
                        raise Exception
                    perimeter = p.triangle(side1, side2, side3)
                    self.label_output.setText(f'Perimeter of triangle is side A + side B + side C\n'
                                      f'{side1} + {side2} + {side3} = {perimeter}\n'
                                      f'Perimeter = {perimeter}')
                else:
                    self.label_output.setText('Please select shape.')
            else:
                self.label_output.setText('Please select area or perimeter.')

        except ValueError:
            self.label_output.setText('Please type in numeric values.')
        except:
            self.label_output.setText('Input values can not be negative.')
        finally:
            self.label_radius.setEnabled(True)
            self.label_side1.setEnabled(True)
            self.label_side2.setEnabled(True)
            self.label_side3.setEnabled(True)
            self.input_radius.setEnabled(True)
            self.input_side1.setEnabled(True)
            self.input_side2.setEnabled(True)
            self.input_side3.setEnabled(True)

            self.input_radius.setText('')
            self.input_side1.setText('')
            self.input_side2.setText('')
            self.input_side3.setText('')