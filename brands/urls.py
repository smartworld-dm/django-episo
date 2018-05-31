from django.urls import path

from articles import views

urlpatterns = [
    path('<slug:name>/', views.show_brand, name="show_brand"),
]