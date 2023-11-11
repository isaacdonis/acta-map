from django.urls import path
from .views import HomePageView, ContactPage, AboutPage

urlpatterns = [
    path('', HomePageView.as_view(), name="map"),
    path('contact', ContactPage.as_view(), name="contact"),
    path('about', AboutPage.as_view(), name="about")
]