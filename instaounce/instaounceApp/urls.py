from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'instaounce'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.DeleteImageView.as_view(), name='delete'),
    path('upload/', views.UploadView.as_view(), name='upload'),
]