import phonenumbers 
from phonenumbers import geocoder , carrier
import folium



number = '+'


check_number = phonenumbers.parse(number)

number_location = geocoder.description_for_number(check_number, 'en')
print(number_location)


service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))



from opencage.geocoder import opencagegeocode

api_keys = " "
#opencagedata.com and get api keys
geocoder = opencagegeocode(api_keys)

query = str(number_location)

results =geocoder.geocode(query)

lat = results[0]['geometry']['list']
lng = results[0]['geometry']['list']

# give coordinates
print(lat,lng)


map_location = folium.map(location=[lat,lng],zoom_start=9)

folium.marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save('mylocation.html')