from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Image
from .forms import UploadImageForm


class IndexView(generic.ListView):
    template_name = 'instaounceApp/index.html'
    context_object_name = 'latest_image_list'

    def get_queryset(self):
        return Image.objects.order_by('-pubDate')[:10]


class DetailView(generic.DetailView):
    model = Image
    template_name = 'instaounceApp/detail.html'


class UploadView(generic.FormView):
    form_class = UploadImageForm
    template_name = 'instaounceApp/upload.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)