from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Url
import random
import string


# Create your views here.
def home(request):
    return render(request, 'home.html')

def _redirect(request, short_url):
    url_obj = Url.objects.get(short_url=short_url)
    url_obj.visits += 1
    url_obj.save()
    return render(request, 'redirect.html', {'url': url_obj.original_url})

def generate_short_url():
    length = 8
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(length))
    return short_url


def create_short_url(request):
    if request.method == 'POST':
        url=request.POST['url']
        short_url=generate_short_url()
        base_url = request.build_absolute_uri('/')
        url_obj = Url.objects.create(original_url=url, short_url=short_url)
        full_short_url = base_url + url_obj.short_url 
        return HttpResponse(f"Short url for {url_obj.original_url} is <a href='{full_short_url}'>{full_short_url}</a>")
    return HttpResponse("Create short url")


def loginform(request):
    return render(request, 'login.html')