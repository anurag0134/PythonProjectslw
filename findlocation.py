import requests
from geopy.geocoders import Nominatim
import pyttsx3
def get_coordinates():
    # Get the device's IP-based location data
    response = requests.get("https://ipinfo.io")
    data = response.json()
    # Extract the coordinates
    loc = data['loc'].split(',')
    latitude = float(loc[0])
    longitude = float(loc[1])
    return latitude, longitude

def get_location(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((latitude, longitude), language='en')
    return location.address if location else "Location not found"

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    latitude, longitude = get_coordinates()
    location = get_location(latitude, longitude)
    output = f"Your current location is: {location}, with coordinates: latitude {latitude}, longitude {longitude}"
    print(output)
    speak_text(output)