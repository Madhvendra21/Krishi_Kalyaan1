from geopy.geocoders import Nominatim

def get_latitude_longitude(city_name):
  """
  This function takes a city name as input and returns its latitude and longitude.

  Args:
      city_name: The name of the city (including country if needed for disambiguation)

  Returns:
      A tuple containing latitude and longitude (or None if location not found).
  """


  geolocator = Nominatim(user_agent="your_app_name")

  location = geolocator.geocode(city_name)

  
  return location.latitude, location.longitude


