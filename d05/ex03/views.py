from django.shortcuts import render
from .models import Movies
from django.conf import settings
import psycopg2


MOVIES = [
    {
        'episode_nb': 4,
        'title': 'A New Hope',
        'director': 'George Lucas',
        'producer': 'Gary Kurtz, Rick McCallum',
        'release_date': '1977-05-25',
    },
    {
        'episode_nb': 5,
        'title': 'The Empire Strikes Back',
        'director': 'Irvin Kershner',
        'producer': 'Gary Kurtz, Rick McCallum',
        'release_date': '1980-05-17',
    }
]

# Create your views here.
def populate_view(request):
    message = "nothing to add"
    try:
        for mv in MOVIES:
            if Movies.objects.filter(episode_nb=mv.get('episode_nb')):
                continue               
            Movies.objects.create(
                episode_nb=mv.get('episode_nb'),
                title=mv.get('title'),
                director=mv.get('director'),
                producer=mv.get('producer'),
                release_date=mv.get('release_date')
            )
            message = None
        status = True
    except Exception as error:
        print(f"ERROR> {error}")
        status = False
        message = "Произошла ошибка"
    return render(request, "ex00/index.html", context={"status":status, "message":message})


def display_view(request):
    selected_fields = Movies.objects.all()
    # print(selected_fields)
    return render(
        request,
        "ex03/display.html",
        context={
            "data":selected_fields
        }
    )