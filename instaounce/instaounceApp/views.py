from django.http import Http404
from django.shortcuts import render
from .models import Image

def index(request):
    latest_image_list = Image.objects.order_by('-pubDate')[:5]
    context = {'latest_image_list': latest_image_list,}
    return render(request, 'instaounceApp/index.html', context)

def detail(request, imageId):
    try: 
        image = Image.objects.get(pk=imageId)
    except Image.DoesNotExist:
        raise Http404("Image does not exist")
    return render(request, 'instaounceApp/detail.html', {'image': image})
