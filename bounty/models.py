import urllib
import json
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

#from django.contrib.gis.geos import Point

#from django.contrib.gis.db import models

def geocode(address):
    formatted_address = address.replace(" ", "+")
    api_key = "AIzaSyDeoNfGCkj0wKpeS15cMTY75Iz6bpY5CwY"
    request = "https://maps.googleapis.com/maps/api/geocode/json?address=" + formatted_address + "&key=" + api_key
    response = urllib.request.urlopen(request)
    str_response = response.readall().decode('utf-8')
    obj = json.loads(str_response)
    lat = obj["results"][0]["geometry"]["location"]["lat"]
    lon = obj["results"][0]["geometry"]["location"]["lng"]
    components = obj["results"][0]["address_components"]
    street = ""
    for component in components:
        component_type = component["types"][0]
        if component_type.lower() == "route":
            street = component["short_name"]
            break
    return lat, lon, street

#class WorldBorder(models.Model):
#    name = models.CharField(max_length=50)
#    area = models.IntegerField()
#    pop2005 = models.IntegerField('Population 2005')
#    fips = models.CharField('FIPS Code', max_length=2)
#    iso2 = models.CharField('2 Digit ISO', max_length=2)
#    iso3 = models.CharField('3 Digit ISO', max_length=3)
#    un = models.IntegerField('United Nations Code')
#    region = models.IntegerField('Region Code')
#    subregion = models.IntegerField('Sub-Region Code')
#    lon = models.FloatField()
#    lat = models.FloatField()
#    mpoly = models.MultiPolygonField()
#    objects = models.GeoManager()

#    def __str__(self):
#        return self.name

#class Zipcode(models.Model):
#    code = models.CharField(max_length=5)
#    poly = models.PolygonField()
#    objects = models.GeoManager()

#class Address(models.Model):
#    line1 = models.CharField(max_length=100)
#    line2 = models.CharField(max_length=100)
#    street = models.CharField(max_length=100, default = "")
#    city = models.CharField(max_length=100)
#    state = models.CharField(max_length=2)
#    zipcode = models.ForeignKey(Zipcode)
#    zipcode_str = models.CharField(max_length=5)
#    coordinates = models.PointField()
#    objects = models.GeoManager()

#    def __str__(self):
#        return self.line1 + ", " + self.line2 + ", " + self.city + ", " + self.state + ", " + self.zipcode_str

#    def save(self, *args, **kwargs):
#        if self.coordinates == None:
#            lat, lon, street = geocode(str(self))
#            pnt = Point(lat, lon)
#            self.coordinates = pnt
#            self.street = street
#        super(Address, self).save(*args, **kwargs)

class ChowBountyUser(models.Model):
    user = models.ForeignKey(User)
    special_instructions = models.CharField(max_length=100)
#    address = models.ForeignKey(Address, null=True)
#    objects = models.GeoManager()

class Vendor(models.Model):
    name = models.CharField(max_length=50)
#    address = models.ForeignKey(Address)
    lon = models.FloatField()
    lat = models.FloatField()
#    mpoly = models.MultiPolygonField()
#    objects = models.GeoManager()

    def __str__(self):
        return self.name
    
# Create your models here.

class Bounty(models.Model):
    cb_user = models.ForeignKey(ChowBountyUser)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=5.00)
    creation_date = models.DateTimeField('date created', default=datetime.now)
    expiration_date = models.DateTimeField('expiration date', null = True)#+timedelta(days=7))
    item_count = models.IntegerField(default = 0)
    is_saved = models.BooleanField(default = False)
    is_claimed = models.BooleanField(default = False)
    is_requested = models.BooleanField(default = False)
#    address = models.ForeignKey(Address, null = True)
#    coordinates = models.PointField(null = True)
#    objects = models.GeoManager()

    def save(self, *args, **kwargs):
#        if self.coordinates == None:
#            self.coordinates = self.cb_user.address.coordinates
#        if self.address == None:
#            self.address = self.cb_user.address
        if self.expiration_date == None:
            self.expiration_date = datetime.now() + timedelta(days=7)
        super(Bounty, self).save(*args, **kwargs)
    
class BountyItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_quantity = models.IntegerField(default=1)
    bounty = models.ForeignKey(Bounty)
    image_link = models.CharField(max_length=200, default="")
    save_date = models.DateTimeField('date saved', default=datetime.now)