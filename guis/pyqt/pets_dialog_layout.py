"""Simple example dialog with layouts with PyQt"""
#pylint: disable=c-extension-no-member

import sys
import PyQt6.QtWidgets as pyqt

# pass command line arguments to Qt here
app = pyqt.QApplication([])

main_wnd = pyqt.QDialog()
main_wnd.setWindowTitle("Pet Database")

_dialog_layout = pyqt.QVBoxLayout()
_form_layout = pyqt.QFormLayout()

_age_input = pyqt.QLineEdit()
_form_layout.addRow("Age", _age_input)

_animal_input = pyqt.QComboBox()
_animal_input.addItems(["Dog", "Cat", "Horse"])
_form_layout.addRow("Type", _animal_input)

_gender_group = pyqt.QButtonGroup()
_male_button = pyqt.QRadioButton("Male")
_gender_group.addButton(_male_button)
_female_button = pyqt.QRadioButton("Female")
_gender_group.addButton(_female_button)
_gender_layout = pyqt.QHBoxLayout()
_gender_layout.addWidget(_male_button)
_gender_layout.addWidget(_female_button)
_form_layout.addRow("Gender", _gender_layout)

_ok_button = pyqt.QPushButton("OK")

_dialog_layout.addLayout(_form_layout)
_dialog_layout.addWidget(_ok_button)
main_wnd.setLayout(_dialog_layout)

main_wnd.show()     # schedules paint event in event queue to compose window
_ret = app.exec()   # application event loop
sys.exit(_ret)
