from django.urls import path
from .views import HomeView, HelpView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('help/', HelpView.as_view(), name='help'),
]