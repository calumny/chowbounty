from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django import template
from django.utils.six import BytesIO

import dateutil.parser

import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

register = template.Library()

from django.contrib.auth import authenticate, login, logout, get_user

from django.contrib.auth.models import User

from django.core import serializers

from bounty.models import Bounty, BountyItem, ChowBountyUser
#from bounty.forms import WorldBorderForm

from bounty.serializers import BountySerializer, BountyItemSerializer

#from django.contrib.gis.geos import Point
#from django.contrib.gis.measure import D

from django.core import serializers

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def new_bounty(request):
    return render(request, 'bounty/newbounty.html', {})

def show_bounty(request, bounty_id):
    bounty = Bounty.objects.get(pk = bounty_id)
#    form = WorldBorderForm()
    return render(request, 'bounty/showbounty.html', {'bounty_items' :  BountyItem.objects.filter(bounty = bounty)})

def list_bounties(request):
    return render(request, 'bounty/localbounties.html', {})


def rest_bounties_list(request):
    if request.method == 'GET':
        bounties = Bounty.objects.all()
        serializer = BountySerializer(bounties, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
@api_view(['POST'])
def post_bounty(request):
    if request.method == 'POST': 
        serializer = BountySerializer(data=request.data)
        if serializer.is_valid():
            bounty = serializer.save()
            for bountyitem in request.data['bountyitem_set']:
                item_serializer = BountyItemSerializer(data = bountyitem)
                if item_serializer.is_valid():
                    item = item_serializer.save(bounty=bounty)
            return HttpResponse(bounty.id)
        else:
            return HttpResponse(serializer.errors)
    else:
        return HttpResponse("No dice")
        

def local_bounties(request):
    miles = request.GET['miles']
    lat = request.GET['lat']
    lng = request.GET['lng']
    pnt = Point(float(lat), float(lng))
    
    local_bounty_list = Bounty.objects.all()
#    local_bounty_list = Bounty.objects.filter(coordinates__distance_lte=(pnt, D(mi = miles))).distance(pnt).order_by('distance')

    data = serializers.serialize("json", local_bounty_list)
    
    dists = []
    items = []
    
    for bounty in local_bounty_list:
#        dist = []
#        dist.append(bounty.coordinates.distance(pnt))
#        dist.append(bounty.address.zipcode_str)
#        dist.append(bounty.address.street)
#        dists.append(dist)
        bounty_items = []
        for bountyItem in  BountyItem.objects.filter(bounty = bounty):
            item_str = bountyItem.item_name + " x" + str(bountyItem.item_quantity)
            bounty_items.append(item_str)
        items.append(bounty_items)
#        bounty_items = BountyItem.objects.filter(bounty = bounty)
    
    return HttpResponse(json.dumps({"bounties": data, "distances": dists, "items": items}))

def default_bounties(request):
    miles = request.GET['miles']
    u = get_user(request)
    cb = ChowBountyUser.objects.get(user = u)    
#    pnt = cb.coordinates
    
    local_bounty_list = Bounty.objects.all()
#    local_bounty_list = Bounty.objects.filter(coordinates__distance_lte=(pnt, D(mi = miles))).distance(pnt).order_by('distance')

    data = serializers.serialize("json", local_bounty_list)
    
    return HttpResponse(json.dumps({"bounties": data, "items": "esrfd"}))

def my_bounties(request):
    u = get_user(request)
    cb = ChowBountyUser.objects.get(user = u)
    bounty_list = Bounty.objects.filter(cb_user = cb)

def add_bounty(request):
    u = get_user(request)
    cb = ChowBountyUser.objects.get(user = u)
    items = request.POST['items']
    date = request.POST['date']
    time = request.POST['time']
    
    expiration = dateutil.parser.parse(date + " " + time)
    
    json_items = json.loads(items)
    bounty = Bounty(cb_user = cb, expiration_date = expiration)
    bounty.save()
    item_count = 0;
    for key in json_items:
        quantity = 1
        try:
            quantity = int(json_items[key])
        except:
            quantity = 1
        if quantity < 1:
            quantity = 1
        bountyItem = BountyItem(item_name = key, item_quantity = quantity, bounty = bounty)
        item_count += quantity
        bountyItem.save()
    bounty.item_count = item_count
    bounty.save()
    return HttpResponse(bounty.id)

def edit_address(request):
    return render(request, 'bounty/edit_address.html', {})

def save_address(request):
#    u = get_user(request)
#    line1 = request.POST['line1']
#    line2 = request.POST['line2']
#    city = request.POST['city']
#    state = request.POST['state']
#    zip_code = request.POST['zip']
#    cb = ChowBountyUser.objects.get(user = u)
#    address = cb.address
#    if address == None:
#        address = Address(line1 = line1, line2 = line2, city = city, state = state, zipcode_str = zip_code)
#    else:
#        address.line1 = line1
#        address.line2 = line2
#        address.city = city
#        address.state = state
#        address.zipcode_str = zip_code
#    address.save()
#    cb.address = address
#    cb.save()
    return HttpResponse(1)