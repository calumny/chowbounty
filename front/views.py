from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django import template

register = template.Library()

from django.contrib.auth import authenticate, login, logout, get_user

from django.contrib.auth.models import User

from django.core import serializers

from bounty.models import ChowBountyUser



def index(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'front/index.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('front:index'))
    
@register.inclusion_tag('login.html') 
def login_form(request):
    username = request.POST['username']
    password = request.POST['password1']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            
            cb = ChowBountyUser.objects.get(user = user)
#            if cb.address == None:
#                return HttpResponseRedirect(reverse('bounty:edit_address'))
#            else:
            return HttpResponseRedirect(reverse('front:index'))
            # Redirect to a success page.
        else:
            return HttpResponseRedirect(reverse('front:index'))
            # Return a 'disabled account' error message
    else:
            return HttpResponseRedirect(reverse('front:index'))
            # Return an 'invalid login' error message.
            

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            cb = ChowBountyUser(user = new_user)
            cb.save()
            return login_form(request)
    else:
        form = UserCreationForm()
    return render(request, "front/register.html", {
        'form': form,
    })

