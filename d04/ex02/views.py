from django.shortcuts import render, redirect
from .forms import DataForm
from django.conf import settings
from datetime import datetime

def get_history():
    history = ""
    with open(settings.LOG_ROOT, "r") as f:
        history = f.read()
    history_lines = history.split("\n")
    return history_lines


def form_view(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            with open(settings.LOG_ROOT, "a") as f:
                f.write(f"""{datetime.now()}: {form.cleaned_data.get("input_data")}\n""")
            return redirect("/ex02/")
    else:
        form = DataForm()
        history_lines = get_history()
    return render(request, "ex02/input_data.html", context={"form": form, "history_lines": history_lines})

def history(request):
    history_lines = get_history()
    return render(request, "ex02/history_page.html", context={"history_lines": history_lines})
