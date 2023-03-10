from django.urls import path
from ex03.views import populate_view, display_view
from .views import remove_view

urlpatterns = [
    path('populate', populate_view),
    path('display', display_view),
    path('remove', remove_view)
]
