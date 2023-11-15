from django.urls import path
from .views import HomePageView, ContactPage, AboutPage, StationFeedback

urlpatterns = [
    path('', HomePageView.as_view(), name="map"),
    path('contact', ContactPage.as_view(), name="contact"),
    path('about', AboutPage.as_view(), name="about"),
    path('stationfeedback/<int:pk>/', StationFeedback.as_view(), kwargs = {"pk":None}, name="stationfeedback"),
]