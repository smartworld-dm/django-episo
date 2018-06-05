from django.urls import path

from articles import views

urlpatterns = [
	path('', views.index_brand, name="index_brand"),
    path('<slug:name_slug>/', views.show_brand, name="show_brand"),
]