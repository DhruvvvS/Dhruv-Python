# Digital Clock using Python and PyQt5 module
import sys
import os

# Importing necessary modules from PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
# Importing QTimer, QTime, and Qt from PyQt5.QtCore for showing time and setting alignment
from PyQt5.QtCore import QTimer, QTime, Qt

from PyQt5.QtGui import QIcon, QFont, QFontDatabase
# QFontDatabase: provides information about the fonts available in the system and allows you to load custom fonts.

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        # Create a QLabel to display the time and a QTimer to update the time every second.
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.setWindowIcon(QIcon("digital_clock.jpg"))
        # Set the window icon using an image file named "digital_clock.jpg".
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock') 
        self.setGeometry(600, 400, 400, 150)  # Set the size and position of the window

        vbox = QVBoxLayout()  # Create a vertical box layout
        vbox.addWidget(self.time_label)  # Add the time label to the layout
        self.setLayout(vbox)  # Set the layout for the widget

        self.time_label.setAlignment(Qt.AlignCenter)  # Align the time label to the center
        self.time_label.setStyleSheet("font-size: 120px;"
                                      "color: hsl(294, 58%, 53%);")  # Set the font size, color of the time label
        self.setStyleSheet("background-color: black;")  # Set the background color of the widget to black

        # Load the custom font from the file "Orbitron-Bold.ttf" and set it to the time label loading from its relative path
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(BASE_DIR, "Orbitron-Bold.ttf")

        font_id = QFontDatabase.addApplicationFont(font_path)  # Load the custom font from the file "Orbitron-Bold.ttf" from its font path
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family)
            self.time_label.setFont(my_font)  # Set the loaded custom font to the time label
        else:
            print("Failed to load font.")  # Print an error message if the font fails to load
        
        self.timer.timeout.connect(self.update_time)  # Connect the timer's timeout signal to the update_time method
        self.timer.start(1000)  # Start the timer to update every 1000 milliseconds (1 second)

        self.update_time()  # Call the update_time method to display the current time immediately

    def update_time(self):
        current_time = QTime.currentTime()  # Get the current time
        display_time = current_time.toString('hh:mm:ss AP')  # Format the time as hh:mm:ss, 
        # here hh is for hours, mm is for minutes and ss is for seconds and AP for AM/PM and this all are format specifiers
        self.time_label.setText(display_time)  # Set the formatted time to the time label

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()