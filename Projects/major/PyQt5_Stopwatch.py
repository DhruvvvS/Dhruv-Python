# PyQt5 Stopwatch Program
# This program creates a stopwatch using PyQt5. It allows the user to start, stop, and reset the stopwatch. 
# The time is displayed in hours, minutes, seconds, and milliseconds.

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)  # Initialize the time to 00:00:00.00
        self.time_label = QLabel("00:00:00.00", self)  # Create a QLabel to display the time
        self.start_button = QPushButton("Start", self)  # Create a Start button
        self.stop_button = QPushButton("Stop", self)  # Create a Stop button
        self.reset_button = QPushButton("Reset", self)  # Create a Reset button
        self.timer = QTimer(self)  # Create a QTimer to update the time
        self.initUI()  # Initialize the user interface

    def initUI(self):
        self.setWindowTitle('Stopwatch')  # Set the window title
        self.setGeometry(600, 400, 400, 150)  # Set the size and position of the window

        vbox = QVBoxLayout()  # Create a vertical box layout
        vbox.addWidget(self.time_label)  # Add the time label to the layout

        self.setLayout(vbox)  # Set the layout for the widget

        self.time_label.setAlignment(Qt.AlignCenter)  # Align the time label to the center

        hbox = QHBoxLayout()  # Create a horizontal box layout for the buttons
        hbox.addWidget(self.start_button)  # Add the Start button to the horizontal layout
        hbox.addWidget(self.stop_button)  # Add the Stop button to the horizontal layout
        hbox.addWidget(self.reset_button)  # Add the Reset button to the horizontal layout
        vbox.addLayout(hbox)  # Add the horizontal layout to the vertical layout

        self.setStyleSheet("""
            QPushButton, QLabel {
                font-family: Calibri;
                font-weight: bold;
                padding: 10px;
                border-radius: 15px;
            }
            QLabel {
                font-size: 100px;
                background-color: hsl(177, 85%, 67%);
            }
            QPushButton {
                font-size: 40px;
                border: 1px solid black;
            }""")
        
        self.start_button.clicked.connect(self.start)  # Connect the Start button's clicked signal to the start method
        self.stop_button.clicked.connect(self.stop)  # Connect the Stop button's clicked signal to the stop method
        self.reset_button.clicked.connect(self.reset)  # Connect the Reset button's clicked signal to the reset method
        self.timer.timeout.connect(self.update_time)  # Connect the timer's timeout signal to the update_time method

    # This method starts the timer to update every 10 milliseconds (0.01 seconds) when the Start button is clicked.
    def start(self):
        self.timer.start(10)  # Start the timer to update every 10 milliseconds (0.01 seconds)

    # This method stops the timer when the Stop button is clicked.
    def stop(self):
        self.timer.stop()

    # This method resets the time to 00:00:00.00 and updates the time label when the Reset button is clicked.
    def reset(self):
        self.timer.stop()  # Stop the timer
        self.time = QTime(0, 0, 0, 0)  # Reset the time to 00:00:00.00
        self.time_label.setText(self.format_time(self.time))  # Update the time label to show the reset time

    # This method formats the time to be displayed in the format "hh:mm:ss.ms" where hh is hours, mm is minutes, ss is seconds and ms is milliseconds.
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 # Convert milliseconds to centiseconds (0.01 seconds) and not show three digits for milliseconds.
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        # 02d is a format specifier that means to format the number as a two-digit decimal, padding with zeros if necessary.

    # This method updates the time by adding 10 milliseconds to the current time and then updates the time label with the formatted time.
    def update_time(self):
        self.time = self.time.addMSecs(10)  # Add 10 milliseconds to the current time
        self.time_label.setText(self.format_time(self.time))  # Update the time label with the formatted time


def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()