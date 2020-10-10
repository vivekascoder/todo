from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return redirect("register")
    form = UserCreationForm()
    return render(request, 'registration/register.html', context = {'form': form})