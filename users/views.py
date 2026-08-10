from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Medicine


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/admin/")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def search_medicine(request):
    query = request.GET.get("q", "").strip()

    medicines = Medicine.objects.filter(
        name__icontains=query
    )

    return render(
        request,
        "search.html",
        {
            "medicines": medicines,
            "query": query,
        }
    )


def nearby_stores(request):
    medicines = Medicine.objects.all()

    return render(
        request,
        "nearby_stores.html",
        {
            "medicines": medicines,
        }
    )
    