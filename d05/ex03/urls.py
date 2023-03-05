from django.urls import path
from .views import populate_view, display_view


urlpatterns = [
    path('populate', populate_view),
    path('display', display_view)
]
