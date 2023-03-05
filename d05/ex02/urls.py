from django.urls import path
from .views import populate, display
from ex00.views import init

urlpatterns = [
    path('init', init, {"table_name": "ex03_movies"}),
    path('populate', populate, {"table_name": "ex02_movies"}),
    path('display', display, {"table_name": "ex02_movies"})
]
