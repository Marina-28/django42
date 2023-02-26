from django.shortcuts import render

# Create your views here.
def table(request):
    return render(request, "ex03/table.html", context={"colors": [i for i in range(255)]})