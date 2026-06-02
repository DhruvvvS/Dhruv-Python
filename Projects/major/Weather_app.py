# WEATHER APP WITH API USING PyQt5

import sys
import os

import requests

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel)

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: " , self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather" , self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 300, 500, 620)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "WeatherApp.png")

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"⚠️ Icon not found at: {icon_path}")
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        vbox.setSpacing(15)
        vbox.setContentsMargins(30, 30, 30, 30)

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
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a2e, stop:1 #16213e
                );
            }
            QLabel, QLineEdit, QPushButton {
                font-family: 'Segoe UI', Arial, sans-serif;
                color: white;
            }
            QLabel#city_label {
                font-size: 30px;
                font-weight: bold;
                color: #e0e0e0;
                letter-spacing: 1px;
            }
            QLineEdit#city_input {
                font-size: 22px;
                padding: 12px 18px;
                border: 2px solid rgba(255,255,255,0.2);
                border-radius: 25px;
                background: rgba(255,255,255,0.1);
                color: white;
            }
            QLineEdit#city_input:focus {
                border: 2px solid rgba(255,255,255,0.6);
                background: rgba(255,255,255,0.15);
            }
            QPushButton#get_weather_button {
                font-size: 20px;
                font-weight: bold;
                padding: 12px 22px;
                border: none;
                border-radius: 25px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4facfe, stop:1 #00f2fe);
                color: #1a1a2e;
            }
            QPushButton#get_weather_button:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #74c8ff, stop:1 #40f7ff);
            }
            QLabel#temperature_label {
                font-size: 70px;
                font-weight: bold;
                color: white;
            }
            QLabel#emoji_label {
                font-size: 90px;
                font-family: "Segoe UI Emoji";
            }
            QLabel#description_label {
                font-size: 30px;
                color: rgba(255,255,255,0.8);
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    def get_weather(self):
        
        api_key = "e7c1c2b414e88dd8d9990d183b61b3e3"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check the city name and try again.")
                case 401:
                    self.display_error("Unauthorized\nPlease check your API key.")
                case 403:
                    self.display_error("Forbidden\nYou don't have permission to access this resource.")
                case 404:
                    self.display_error("City not found\nPlease check the city name and try again.")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later.")
                case 502:
                    self.display_error("Bad Gateway\nPlease try again later.")
                case 503:
                    self.display_error("Service Unavailable\nServer is down.")
                case 504:
                    self.display_error("Gateway Timeout\nPlease try again later.")
                case _:
                    self.display_error(f"HTTP error occurred\n{response.status_code}")
        
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error\nPlease check your internet connection and try again.")

        except requests.exceptions.Timeout:
            self.display_error("Request timed out\nPlease try again later.")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nPlease check the URL and try again.")

        except requests.exceptions.RequestException as e:
            self.display_error(f"An error occurred\n{e}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 70px; font-weight: bold;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if weather_id >= 200 and weather_id <= 232:
            return "⛈️"
        elif weather_id >= 300 and weather_id <= 321:
            return "🌦️"
        elif weather_id >= 500 and weather_id <= 531:
            return "🌧️"
        elif weather_id >= 600 and weather_id <= 622:
            return "❄️"
        elif weather_id >= 700 and weather_id <= 781:
            return "🌫️"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id >= 801 and weather_id <= 804:
            return "☁️"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())