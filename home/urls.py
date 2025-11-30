from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("problem", views.problem, name='problem')
]