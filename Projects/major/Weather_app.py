# WEATHER APP WITH API USING PyQt5

# importing sys module to access command-line arguments and exit the application properly.
import sys

# importing os for file path of the Icon.
import os

# importing requests module to make HTTP requests to the weather API.
import requests

# importing necessary modules from PyQt5 packages.
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel)

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QIcon

# Weather App Class
class WeatherApp(QWidget):
    def __init__(self):
        # setting up all labels and buttons in the constructor and then calling the initUI method to set up the user interface.
        super().__init__()
        self.city_label = QLabel("Enter city name: " , self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather" , self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    # initUI method is responsible for setting up the user interface of the application, including window properties, layout, widget styling, and signal connections.
    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 300, 500, 620)

        # Setting the window icon using an image file "WeatherApp.png". 
        # The code constructs the file path to the icon and checks if it exists before setting it. If the icon is not found, it prints a warning message.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "WeatherApp.png")

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"⚠️ Icon not found at: {icon_path}")

        # Creating a vertical box layout to arrange the widgets vertically and adding the widgets to the layout.
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

        # Aligning all widgets to the center.
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Setting object names for styling purposes in the stylesheet.
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # CSS stylesheet to style the widgets with a modern look, including background gradients, font styles, colors, padding, borders, and hover effects for the button.
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

        # Connecting the clicked signal of the "Get Weather" button and the returnPressed signal of the city input field to the get_weather method,
        # which will be called when the user clicks the button or presses Enter after typing a city name.
        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    # get_weather method is responsible for making the API request to fetch weather data based on the city name entered by the user,
    # handling various exceptions that may occur during the request, and displaying either the weather information or appropriate error messages.
    def get_weather(self):
        
        # API key and city name are defined, and the URL for the API request is constructed using an f-string. 
        api_key = "e7c1c2b414e88dd8d9990d183b61b3e3"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        # GET request to the API using the requests library. If the request is successful and the API returns a valid response, it calls the display_weather method to show the weather information.
        try:
            response = requests.get(url)
            # raise_for_status() is called to check if the HTTP request was successful. If the response status code indicates an error (e.g., 4xx or 5xx), it raises an HTTPError exception, which is caught and handled in the except block.
            response.raise_for_status()
            data = response.json()

            # The code checks if the "cod" field in the API response is 200, which indicates a successful response with valid weather data. If so, it calls the display_weather method to show the weather information on the GUI.
            if data["cod"] == 200:
                self.display_weather(data)
        
        # The code includes multiple except blocks to handle different types of exceptions that may occur during the API request.
        # HTTPError is handled to provide specific error messages based on the status code returned by the API, such as 400 for bad requests, 401 for unauthorized access, 404 for city not found, and various server errors.
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
        
        # ConnectionError is handled to inform the user about issues with their internet connection.
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error\nPlease check your internet connection and try again.")

        # Timeout is handled to inform the user that the request took too long and to try again later.
        except requests.exceptions.Timeout:
            self.display_error("Request timed out\nPlease try again later.")

        # TooManyRedirects is handled to inform the user about issues with the URL and to check it before trying again.
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nPlease check the URL and try again.")

        # A general exception handler is included to catch any other types of exceptions that may occur during the API request and to display a generic error message with the exception details.
        except requests.exceptions.RequestException as e:
            self.display_error(f"An error occurred\n{e}")

    # display_error method is responsible for displaying error messages on the GUI when an error occurs during the API request. It updates the temperature label to show the error message and clears the emoji and description labels.
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    # display_weather method is responsible for displaying the weather information on the GUI when a successful API response is received. It extracts the temperature in Kelvin from the API response, converts it to Celsius, and updates the temperature label with the formatted temperature.
    # It also retrieves the weather condition ID and description from the API response, updates the emoji label with an appropriate weather emoji based on the condition ID, and sets the description label with the weather description.
    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 70px; font-weight: bold;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    # get_weather_emoji is a static method that takes a weather condition ID as input and returns an appropriate weather emoji based on the ID.
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

# The main block of the code creates an instance of the QApplication, initializes the WeatherApp, shows the application window, and starts the event loop to keep the application running until the user closes it.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())