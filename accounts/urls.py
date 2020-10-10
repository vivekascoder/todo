from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register', accounts_views.register_view, name="register")
]