from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView

from .models import Image
from .forms import UploadImageForm

class Login(LoginView):
    template_name = 'instaounceApp/login.html'


class IndexView(generic.ListView):
    template_name = 'instaounceApp/index.html'
    context_object_name = 'latest_image_list'

    def get_queryset(self):
        return Image.objects.order_by('-pubDate')[:10]


class DetailView(generic.DetailView):
    model = Image
    template_name = 'instaounceApp/detail.html'


class UploadView(generic.CreateView):
    form_class = UploadImageForm
    template_name = 'instaounceApp/upload.html'
    model = Image
    success_url = '/instaounceApp'

        