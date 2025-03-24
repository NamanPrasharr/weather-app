import requests
import json
import pyttsx3  

engine = pyttsx3.init()  


city = input("Enter the Name of the City:   ")

url = f"https://api.weatherapi.com/v1/current.json?key=5d6d981d57fd4344ab7150052252403&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = (wdic["current"]["temp_c"])
t = (wdic["location"]["localtime"])

x = (f"The current weather in {city} at {t} is {w} degrees")
engine.say(x)
engine.runAndWait()
