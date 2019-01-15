from geopy.geocoders import Nominatim
import folium
from folium import plugins

import string
from mongodb_atlas import connect_db

#RETRIEVE ALL DISEASE DETAILS FROM DB
try:
    arr_loc = connect_db.retrieve_data()
except:
    print("Problem fetching data from db")

m = folium.Map(location=[-20.2759451, 57.5703566])

for data in arr_loc:
    d = data['location']
    if d != "Not found":
        for char in string.punctuation:
            s = d.replace(char, ' ')
        result = ''.join([i for i in s if not i.isdigit()])
        print(result)
    disease = data['diseasetype']
    date = data['date']


    geolocator = Nominatim()
    location = geolocator.geocode(result+ " ,Mauritius")
    print((location.latitude, location.longitude))
    long = location.longitude
    lat = location.latitude


    html="""
        <p>
        Disease alert:"""+disease+""" at """+date +"""
        </p>
    """
    iframe = folium.IFrame(html=html, width=300, height=100)
    popup = folium.Popup(iframe, max_width=1000)

    folium.Marker([lat, long], popup=popup).add_to(m)

m.save("map.html")

# Place map -- using googlemaps API
"""


gmap = gmplot.GoogleMapPlotter(-20, 57, 10)
gmap.marker(lat, long, "FF0000")

gmap.draw("my_map2.html")"""

