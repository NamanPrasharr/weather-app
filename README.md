# Weather Report Using Python

This Python program fetches real-time weather data for a given city using the WeatherAPI and provides an audio output of the weather details using the `pyttsx3` text-to-speech engine.

## Features
- Fetches live weather updates using WeatherAPI.
- Reads out the weather details using text-to-speech.
- Displays weather information such as temperature and local time of the city.

## Requirements
Ensure you have the following Python packages installed:

```bash
pip install requests pyttsx3
```

## How It Works
1. The program prompts the user to enter a city name.
2. It retrieves the weather data from WeatherAPI.
3. The current temperature and local time are extracted from the response.
4. The program prints and reads out the weather details using a text-to-speech engine.

## Usage
Run the script using:

```bash
python weather_app.py
```

### Example Input & Output:
```
Enter the Name of the City: New York
The current weather in New York at 2025-03-18 14:30 is 15.5 degrees
```
_(The program will also read this out loud.)_

## Code
```python
import requests
import json
import pyttsx3  

engine = pyttsx3.init()  

city = input("Enter the Name of the City:   ")

url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
t = (wdic["location"]["localtime"])

x = (f"The current weather in {city} at {t} is {w} degrees")
engine.say(x)
engine.runAndWait()
```

## Notes
- Replace `YOUR_API_KEY` with your own API key from [WeatherAPI](https://www.weatherapi.com/).
- Ensure you have an active internet connection for fetching weather data.
- The program works for any city worldwide.

## Contributing
Feel free to fork this repository and enhance it with additional features like:
- Adding error handling for invalid city names.
- Displaying additional weather details (humidity, wind speed, etc.).

## License
This project is open-source and available under the MIT License.


# weather
