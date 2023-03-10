from django.shortcuts import render, redirect
from ex03.models import Movies
from ex04.forms import RemoveMoveForm

# Create your views here.
def remove_view(request):
    objs = Movies.objects.all()
    if not objs:
        return render(request, "ex04/remove.html", context={"message":"No data available"})
    choices = ((obj.title, obj.title) for obj in objs)

    if request.method == "POST":
        form = RemoveMoveForm(choices, request.POST)
        if form.is_valid():
            objs.filter(title=form.cleaned_data.get("title")).delete()
            return redirect("/ex03/display")
    else:
        form = RemoveMoveForm(choices)
    return render(request, "ex04/remove.html", context={"form":form})