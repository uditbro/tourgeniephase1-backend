from django.urls import path
from . import views
from .views import TripCreateView
# from .views import GenerateItineraryView

urlpatterns = [
    path('create/', TripCreateView.as_view(), name='create-trip'),
    # path('plan/', GenerateItineraryView.as_view(), name='generate-itinerary'),
    path("plan/", views.generate_itinerary_openrouter, name="generate_itinerary_openrouter"),



]

