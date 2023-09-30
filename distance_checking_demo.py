from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="city_distance_calculator")
print("whare from start your journey: ")
city1_name = input()
print("whare you end your journey: ")
city2_name = input()

city1_location = geolocator.geocode(city1_name)
city2_location = geolocator.geocode(city2_name)

if city1_location is not None and city2_location is not None:
    city1_coordinates = (city1_location.latitude, city1_location.longitude)
    city2_coordinates = (city2_location.latitude, city2_location.longitude)

    distance = geodesic(city1_coordinates, city2_coordinates).kilometers
#for ordinary bus
    farePerKm = 3
#for AC bus 
    AcFarePerKm = 10
    fare2 = distance * AcFarePerKm
    fare1 = distance * farePerKm
#for timing
    dist = distance
    speed = 50#kh/h
    take_time = dist/speed
    
    print(f"The distance between {city1_name} and {city2_name} is approximatly {distance} kilometers.")
    print(f"Your journey will be coverd approximately {take_time} hour")
    print(f"your fare of ordinary bus is {fare1} ")
    print(f"your AC bus journey fare is {fare2}")
else:
    print("One or both of the cities couldn't be geocoded.")
