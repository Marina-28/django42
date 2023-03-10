from django.shortcuts import render, redirect
from django.conf import settings
from utils.db_utils import work_with_db
from .forms import RemoveMoveForm


DB_PARAMS = settings.DATABASES.get("default", dict())
# Create your views here.
def remove(request, table_name):
    query = f"SELECT title from {table_name}"
    status, selected_fields = work_with_db(query, DB_PARAMS, SELECT=True)
    if not selected_fields:
        return render(request, "ex04/remove.html", context={"message":"No data available"})
    # print(selected_fields)
    choices = ((line[0], line[0]) for line in selected_fields)
    
    if request.method == "POST":
        form = RemoveMoveForm(choices, request.POST)
        if form.is_valid():
            query = f"""DELETE FROM {table_name} \
WHERE title = '{form.cleaned_data.get("title")}';"""
            # print(query)
            status, selected_fields = work_with_db(query, DB_PARAMS)
            return redirect("/ex04/display")
    else:
        form = RemoveMoveForm(choices)
    return render(request, "ex04/remove.html", context={"form":form})
        