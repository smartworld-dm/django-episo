from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('<int:id>/', views.show, name='show'),
]