from django.shortcuts import render
from .forms import DataForm
from django.conf import settings

# Create your views here.
def form_view(reqquest):
    pass


def history(request):
    history = ""
    with open(settings.LOG_ROOT, "r") as f:
        history = f.read()
    history_lines = history.split("\n")
    return render(request, "ex02/history_page.html", context={'history_lines': history_lines})
