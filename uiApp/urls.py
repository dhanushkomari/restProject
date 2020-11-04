from django.urls import path
from . import views

app_name = 'uiApp'

urlpatterns = [
    path('', views.index, name = "home")
]
