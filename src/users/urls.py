from django.urls import path
from .views import registerView ,profile_view

urlpatterns = [
    path('register/', registerView, name='register'),
    path('profile/', profile_view, name='profile'),
]