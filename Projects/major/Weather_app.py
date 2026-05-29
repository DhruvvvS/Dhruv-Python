# WEATHER APP WITH API USING PyQt5

import sys

import requests

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel)

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: " , self)
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Get Weather" , self)
        self.temperature_label = QLabel("40°C", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 400, 500, 500)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QLineEdit, QPushButton {
                font-family: Arial;
                color: black;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
                padding: 10px;
                border: 2px solid black;
                border-radius: 10px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                padding: 10px;
                border: 2px solid black;
                border-radius: 10px;
                background-color: hsl(202, 92%, 65%);
            }
            QLabel#temperature_label {
                font-size: 70px;
                font-weight: bold;
            }
            QLabel#emoji_label {
                font-size: 90px;
                font-family: "Segoe UI Emoji";
            }
            QLabel#description_label {
                font-size: 50px;
            }
            QPushButton#get_weather_button:hover {
                background-color: hsl(202, 92%, 75%);
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())