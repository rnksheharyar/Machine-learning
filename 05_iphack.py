# import geo
# ip = geo.getIP()
# print(ip)

# country = geo.getCountry(ip, 'plain')
# print(country)
# geoData = geo.getCountry(ip, 'json')
# print(country)
# geoData = geo.getGeoData(ip)
# print(geoData)
# ptrData = geo.getPTR(ip)
# print(ptrData)
# geo.showIpDetails('216.239.32.0')
# geo.ShowCountryDetails('216.239.32.0')
#Importing the Nominatim geocoder class 
from geopy.geocoders import Nominatim
 
#address we need to geocode
loc = 'Taj Mahal, Agra, Uttar Pradesh 282001'
 
#making an instance of Nominatim class
geolocator = Nominatim(user_agent="my_request")
 
#applying geocode method to get the location
location = geolocator.geocode(loc)
 
#printing address and coordinates
print(location.address)
print((location.latitude, location.longitude))