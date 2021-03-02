from django.urls import path, include

from . import views

urlpatterns = [
    # Strona glowna
    path('', views.index, name='index'),
    path('dodaj', views.add_finding, name="add_finding"),
    path('link/<finding_id>/', views.finding, name='finding')

]
