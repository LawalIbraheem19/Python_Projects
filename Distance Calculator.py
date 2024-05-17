from geopy.distance import geodesic

#loading the latitude and longitude from the two locations
first_location = (52.2296756, 21.0122287)
second_location = (52.406374, 16.9251681)

#print distance in km
distance = int(geodesic(first_location, second_location).km)
print(distance, "Kilometres")
