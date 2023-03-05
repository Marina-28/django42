
from django.urls import path
from .views import init

urlpatterns = [
    path('init', init, {"table_name": "ex00_movies"})
]
