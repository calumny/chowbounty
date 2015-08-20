from django.contrib.gis import forms

class WorldBorderForm(forms.Form):
    world = forms.MultiPolygonField(widget = 
        forms.OSMWidget(attrs = {'map_width': 1024, 'map_height': 600, 'default_zoom' : 18, 'default_lat' : 42.36, 'default_lon' : 288.94}))