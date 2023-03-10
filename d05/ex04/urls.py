from django.urls import path
from ex00.views import init
from ex02.views import populate, display
from .views import remove

urlpatterns = [
    path('init', init, {"table_name": "ex04_movies"}),
    path('populate', populate, {"table_name": "ex04_movies"}),
    path('display', display, {"table_name": "ex04_movies"}),
    path('remove', remove, {"table_name": "ex04_movies"})
]
