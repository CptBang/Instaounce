from django.urls import path
from . import views

app_name = 'instaounce'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('upload/', views.UploadView.as_view(), name='upload'),
]