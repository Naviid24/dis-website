from django.urls import path
from .views import home, about, kitchens, bathrooms, quote_view

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("kitchens/", kitchens, name="kitchens"),
    path("bathrooms/", bathrooms, name="bathrooms"),
    path("quote/", quote_view, name="quote"),
]
