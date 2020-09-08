from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Image
from .forms import UploadImageForm


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'instaounceApp/signup.html'
    success_url = '/'

    # def form_valid(self, form):
    #     form.save()
    #     username = form.cleaned_data.get('username')
    #     raw_password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=raw_password)
    #     login(self.request, user)
    #     return redirect('home')


class Login(LoginView):
    template_name = 'instaounceApp/login.html'


class IndexView(generic.ListView):
    template_name = 'instaounceApp/index.html'
    context_object_name = 'latest_image_list'

    def get_queryset(self):
        return Image.objects.order_by('-pubDate')


class ProfileView(generic.ListView):
    template_name = 'instaounceApp/profile.html'
    context_object_name = 'user_uploaded_images'

    def get_queryset(self):
        return Image.objects.filter(author=self.request.user)


class DetailView(generic.DetailView):
    model = Image
    template_name = 'instaounceApp/detail.html'


class UploadView(generic.CreateView):
    form_class = UploadImageForm
    template_name = 'instaounceApp/upload.html'
    model = Image
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteImageView(LoginRequiredMixin, generic.DeleteView):
    model = Image
    template_name = 'instaounceApp/deleteImage.html'
    success_url = '/profile/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponseForbidden("Cannot delete other's posts")
