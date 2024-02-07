from django.urls import path

from .views import AboutPage, ContactPage, HomePageView, station_feedback

urlpatterns = [
    path("", HomePageView.as_view(), name="map"),
    path("contact", ContactPage.as_view(), name="contact"),
    path("about", AboutPage.as_view(), name="about"),
    path("stationfeedback/<int:pk>/", station_feedback, name="stationfeedback"),
]
