from django.urls import path, include

from . import views

urlpatterns = [
    # Strona glowna
    path('', views.index, name='index'),

]
