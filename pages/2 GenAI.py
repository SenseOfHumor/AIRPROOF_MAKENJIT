import streamlit as st
import requests

# Securely load API key from environment variable
from os import getenv

# Set default location (optional, adjust as needed)
default_location = "New York, NY"

def get_geocode(location):
  """Fetches latitude and longitude coordinates for a given location."""
  maps_api_key = getenv("MAPS_API_KEY")
  if not maps_api_key:
    st.error("Please set the 'MAPS_API_KEY' environment variable.")
    return None

  geocoding_endpoint = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={maps_api_key}"
  response = requests.get(geocoding_endpoint)

  if response.status_code == 200:
    data = response.json()
    if data["status"] == "OK":
      # Extract latitude and longitude from the first result
      latitude = data["results"][0]["geometry"]["location"]["lat"]
      longitude = data["results"][0]["geometry"]["location"]["lng"]
      return latitude, longitude
    else:
      st.error(f"Geocoding failed: {data['status']}")
  else:
    st.error(f"Error fetching geocode data: {response.status_code}")
  return None

def visualize_map(location):
  """Displays a Google Static Map centered on the given location."""
  latitude, longitude = get_geocode(location)

  if latitude and longitude:
    static_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=13&size=600x400&key={getenv('MAPS_API_KEY')}"
    st.image(static_map_url)
  else:
    st.warning("Unable to visualize map. Please check the location entered.")

st.title("Location Visualizer")

location_input = st.text_input("Enter a location:", default_location)

if st.button("Visualize"):
  visualize_map(location_input)

