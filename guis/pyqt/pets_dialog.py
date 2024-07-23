"""Simple dialog example with fixed locations using PyQt"""
#pylint: disable=c-extension-no-member

import sys
import PyQt6.QtWidgets as pyqt

# pass command line arguments to Qt here
app = pyqt.QApplication([])

main_wnd = pyqt.QDialog()
main_wnd.setWindowTitle("Pet Database")
main_wnd.setGeometry(50, 60, 500,400)
# add some text (you can also add images)
_age_text = pyqt.QLabel("<b>Age</b>", parent=main_wnd)
_age_text.move(10, 80)
_age_input = pyqt.QLineEdit(parent=main_wnd)
_age_input.move(60, 80)

_animal_text = pyqt.QLabel("<b>Type</b>", parent=main_wnd)
_animal_text.move(10, 120)
_animal_input = pyqt.QComboBox(parent=main_wnd)
_animal_input.addItems(["Dog", "Cat", "Horse"])
_animal_input.move(60, 120)

_gender_group = pyqt.QButtonGroup(parent=main_wnd)
_gender_text = pyqt.QLabel("<b>Gender</b>", parent=main_wnd)
_gender_text.move(10, 160)
_male_button = pyqt.QRadioButton("Male", parent=main_wnd)
_male_button.move(80, 160)
_gender_group.addButton(_male_button)
_female_button = pyqt.QRadioButton("Female", parent=main_wnd)
_female_button.move(160,160)
_gender_group.addButton(_female_button)

_ok_button = pyqt.QPushButton("OK", parent=main_wnd)
_ok_button.move(200,350)

main_wnd.show()     # schedules paint event in event queue to compose window
_ret = app.exec()   # application event loop
sys.exit(_ret)
