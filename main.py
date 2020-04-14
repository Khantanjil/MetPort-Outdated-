# Importing pandas and bokeh
import folium
import requests
from color import *
import pandas


# Map
class Meterology():
    global i

    """
    The map shows the informations of the basics meteorology, if it's rainning return blue on the each country, return yellow if it's a good time!
    """

    # Constructs a base map
    def __init__(self):

        global base_map
        
        """Base map with folium"""
        base_map = folium.Map(
            location = [41.1579, -8.6291],
            min_zoom = 3,
            max_zoom = 10,
            zoom_start = 10,
            tiles = 'OpenStreetMap'
        )

    def saveFile(self):
        """ Save the map file in the html file """
        
        base_map.save("meteo.html")

 
    def populationGroup(self):
        """
        Add the GeoJson layers on the map
        """
        fgP = folium.FeatureGroup(name="Population on the world")
        
        fgP.add_child(folium.GeoJson(data=open('world.json', 'r').read(),
        style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
        else 'red'}))
        base_map.add_child(fgP)

    def portugalGroup(self):
        """GeoJson for portugal"""
        fg_portugal = folium.FeatureGroup(name="Portugal")
        fg_portugal.add_child(folium.GeoJson("portugal.json"), name="geojson")
        base_map.add_child(fg_portugal)
        
    def meteorologia(self):
        data = pandas.read_csv("temps/todaysTemMax.txt")
        lat = list(data["latitude"])
        lon = list(data["longitude"])
        city = list(data["city"])
        temperature = list(data["temperature"])
        for lt, ln, ct, temp in zip(lat, lon, city, temperature):
            html = """<h3>Informations about the %s:</h3>
            <p>The max temperature: %s<p>
            <p>The latitude: %s</p>
            <p>The longitude: %s</p>
            """
                
            iframe = folium.IFrame(html = html % (str(ct), str(temp), str(lt), str(ln)), width=200, height=200)
            fg_met = folium.FeatureGroup(name="Temperatura Máxima")
            fg_met.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),
             fill=True,
             radius=8, fill_color=producerColor(temp), color="black", fill_opacity=1))
            base_map.add_child(fg_met)



    
    def addControl(self):
        """ Add the layer control on the map"""
        folium.LayerControl().add_to(base_map)

    def readInfo(self):
        with open("todaysTemMax.txt", "r+") as file:
            content = file.readlines()
            print(content)